"use server";

import { createClient } from "@/lib/supabase/server";

export async function exportAthleteDataAction() {
  try {
    const supabase = await createClient();
    const {
      data: { user },
    } = await supabase.auth.getUser();

    if (!user) {
      return { success: false, error: "Authentication required for GDPR data export." };
    }

    const { data: profile } = await supabase
      .from("profiles")
      .select("*")
      .eq("id", user.id)
      .single();

    const { data: plans } = await supabase
      .from("performance_plans")
      .select("*")
      .eq("profile_id", user.id);

    const { data: reflections } = await supabase
      .from("weekly_reflections")
      .select("*")
      .eq("profile_id", user.id);

    const { data: progress } = await supabase
      .from("participant_progress")
      .select("*")
      .eq("profile_id", user.id);

    // Record GDPR export compliance log
    await supabase.from("gdpr_compliance_requests").insert({
      profile_id: user.id,
      request_type: "export",
      status: "completed",
      details: { export_requested_at: new Date().toISOString() },
    });

    const exportBundle = {
      complianceStandard: "EU General Data Protection Regulation (GDPR) Article 15 & 20",
      dataSubjectId: user.id,
      exportedAt: new Date().toISOString(),
      profile: profile || {},
      performancePlans: plans || [],
      weeklyReflections: reflections || [],
      progressRecords: progress || [],
    };

    return {
      success: true,
      data: exportBundle,
    };
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Failed to generate GDPR export";
    return { success: false, error: message };
  }
}

export async function requestErasureAction() {
  try {
    const supabase = await createClient();
    const {
      data: { user },
    } = await supabase.auth.getUser();

    if (!user) {
      return { success: false, error: "Authentication required for erasure request." };
    }

    // Record GDPR Erasure Request
    await supabase.from("gdpr_compliance_requests").insert({
      profile_id: user.id,
      request_type: "erasure",
      status: "pending_review",
      details: {
        requested_at: new Date().toISOString(),
        notice: "Participant requested complete erasure under GDPR Article 17.",
      },
    });

    return {
      success: true,
      message:
        "Your GDPR Article 17 erasure request has been submitted to the Lornette’s Foundation compliance office. All private reflections and identifying telemetry will be purged in accordance with statutory privacy obligations.",
    };
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Failed to record erasure request";
    return { success: false, error: message };
  }
}
