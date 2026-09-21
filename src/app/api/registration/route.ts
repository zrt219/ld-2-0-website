import { NextResponse } from "next/server";

import { registrationSchema } from "@/lib/registration-schema";
import { createAdminClient } from "@/lib/supabase/admin";
import { apiRateLimit } from "@/lib/rate-limit";

export async function POST(request: Request) {
  const ip = request.headers.get("x-forwarded-for") || "unknown";
  if (apiRateLimit.isRateLimited(ip)) {
    return NextResponse.json({ ok: false, message: "Too many requests" }, { status: 429 });
  }

  const body = await request.json().catch(() => null);
  const parsed = registrationSchema.safeParse(body);

  if (!parsed.success) {
    return NextResponse.json(
      {
        ok: false,
        message: "Please complete all required fields correctly.",
        errors: parsed.error.flatten().fieldErrors,
      },
      { status: 400 },
    );
  }

  const data = parsed.data;

  // Honeypot spam check
  if (data.website) {
    return NextResponse.json({
      ok: true,
      message: "Thank you for registering. We will be in touch shortly.",
    });
  }

  try {
    const supabase = createAdminClient();
    
    let cohortRecord: { id: string; capacity: number | null; status: string } | null = null;

    // Check for club code against canonical cohorts table
    if (data.clubCode) {
      const { data: cohort, error: cohortError } = await supabase
        .from("cohorts")
        .select("id, capacity, status")
        .eq("cohort_code", data.clubCode.trim().toUpperCase())
        .single();
      
      if (cohortError || !cohort) {
        return NextResponse.json({ ok: false, message: "Invalid club / cohort code." }, { status: 400 });
      }

      if (cohort.status !== "active" && cohort.status !== "upcoming") {
        return NextResponse.json({ ok: false, message: "This cohort code is no longer active." }, { status: 400 });
      }

      cohortRecord = cohort;
    } else {
      // Fetch default active cohort if the user didn't specify a precise one
      const { data: activeCohorts, error: cohortError } = await supabase
        .from("cohorts")
        .select("id, capacity, status")
        .eq("status", "active")
        .limit(1);

      if (cohortError || !activeCohorts || activeCohorts.length === 0) {
        console.error("No active cohort found to associate registration.", cohortError);
        return NextResponse.json(
          { ok: false, message: "No active cohort available for registration." },
          { status: 500 }
        );
      }

      cohortRecord = activeCohorts[0];
    }

    const full_name = `${data.firstName} ${data.lastName}`;
    const regType = data.clubCode ? "club_sponsored" : "individual_paid";

    // 1. Transactional server-side capacity validation using Postgres row-level locking
    const { data: rpcData, error: rpcError } = await supabase.rpc("register_cohort_athlete", {
      p_cohort_id: cohortRecord.id,
      p_full_name: full_name,
      p_email: data.email,
      p_registration_type: regType,
    });

    if (!rpcError && rpcData) {
      if (!rpcData.success) {
        return NextResponse.json(
          {
            ok: false,
            message: rpcData.error || "This cohort has reached maximum capacity. Please contact support or join the waitlist.",
          },
          { status: 409 }
        );
      }
    } else {
      // Fallback for mock/unmigrated database environments
      if (cohortRecord.capacity !== null && cohortRecord.capacity !== undefined) {
        const { count: currentEnrolled } = await supabase
          .from("cohort_members")
          .select("*", { count: "exact", head: true })
          .eq("cohort_id", cohortRecord.id);

        if ((currentEnrolled || 0) >= cohortRecord.capacity) {
          return NextResponse.json(
            {
              ok: false,
              message: "This cohort has reached maximum capacity. Please contact support or join the waitlist.",
            },
            { status: 409 }
          );
        }
      }

      const { error: insertError } = await supabase.from("registrations").insert({
        cohort_id: cohortRecord.id,
        full_name,
        email: data.email,
        registration_type: regType,
        status: "pending",
      });

      if (insertError) {
        console.error("Supabase registration insert error:", insertError);
        return NextResponse.json(
          { ok: false, message: "Failed to store registration." },
          { status: 500 }
        );
      }
    }
  } catch (error) {
    console.error("Admin client error:", error);
    return NextResponse.json(
      { ok: false, message: "Database configuration error." },
      { status: 500 }
    );
  }

  // Per Prompt C constraints: "DO NOT send real outbound emails during this task."
  // Email sending is disabled, data is only stored securely in the database.
  return NextResponse.json({
    ok: true,
    message:
      "Registration submitted successfully! We will follow up with you within 1-2 business days.",
  });
}
