import { NextResponse } from "next/server";

import { inquirySchema } from "@/lib/inquiry-schema";
import { createAdminClient } from "@/lib/supabase/admin";
import { apiRateLimit } from "@/lib/rate-limit";

export async function POST(request: Request) {
  const ip = request.headers.get("x-forwarded-for") || "unknown";
  if (apiRateLimit.isRateLimited(ip)) {
    return NextResponse.json({ ok: false, message: "Too many requests" }, { status: 429 });
  }

  const body = await request.json().catch(() => null);
  const parsed = inquirySchema.safeParse(body);

  if (!parsed.success) {
    return NextResponse.json(
      {
        ok: false,
        message: "Please correct the highlighted fields.",
        errors: parsed.error.flatten().fieldErrors,
      },
      { status: 400 },
    );
  }

  const inquiry = parsed.data;

  if (inquiry.website) {
    return NextResponse.json({
      ok: true,
      message: "Inquiry received.",
    });
  }

  const subject = `Booking inquiry for Lornette Daye: ${inquiry.eventType}`;
  const message = JSON.stringify(inquiry, null, 2);

  try {
    const supabase = createAdminClient();
    const { error } = await supabase.from("inquiries").insert({
      subject,
      message,
      status: "pending",
    });

    if (error) {
      console.error("Supabase error:", error);
      return NextResponse.json(
        { ok: false, message: "Failed to store inquiry." },
        { status: 500 }
      );
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
  return NextResponse.json({ ok: true, message: "Inquiry sent." });
}
