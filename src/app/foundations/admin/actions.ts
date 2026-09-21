"use server";

import { createClient } from "@/lib/supabase/server";
import { cookies } from "next/headers";
import { revalidatePath } from "next/cache";

export async function createCohortAction(formData: FormData) {
  const cookieStore = await cookies();
  const hasAdminCookie = cookieStore.get("ld_admin_access")?.value === "true";

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user && !hasAdminCookie) return;

  const title = formData.get("title") as string;
  const cohort_code = (formData.get("cohort_code") as string)?.trim().toUpperCase();
  const start_date = formData.get("start_date") as string;

  try {
    const { data: program } = await supabase
      .from("programs")
      .select("id")
      .eq("slug", "lornettes-foundation-golf")
      .single();

    const { data: version } = await supabase
      .from("program_versions")
      .select("id")
      .eq("program_id", program?.id)
      .single();

    const rawCapacity = formData.get("capacity") as string;
    const capacity =
      rawCapacity === "unlimited" || rawCapacity === "null"
        ? null
        : rawCapacity && !isNaN(Number(rawCapacity))
        ? Math.max(1, parseInt(rawCapacity, 10))
        : 20;

    if (program && version && title && cohort_code && start_date) {
      await supabase.from("cohorts").insert({
        program_id: program.id,
        program_version_id: version.id,
        title,
        cohort_code,
        start_date,
        capacity,
        status: "active",
      });
    }
  } catch {
    // Fallback if Supabase is offline
  }

  revalidatePath("/foundations/admin");
}

export async function submitReviewAction(formData: FormData) {
  const cookieStore = await cookies();
  const hasAdminCookie = cookieStore.get("ld_admin_access")?.value === "true";

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user && !hasAdminCookie) return;

  const plan_id = formData.get("plan_id") as string;
  const review_notes = formData.get("review_notes") as string;

  if (plan_id && review_notes) {
    try {
      await supabase.from("mentor_reviews").insert({
        plan_id,
        reviewer_id: user?.id || "admin-coach-lornette",
        review_notes,
      });
    } catch {
      // Fallback if Supabase is offline
    }
  }

  revalidatePath("/foundations/admin");
}

