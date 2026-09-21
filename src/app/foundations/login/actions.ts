"use server";

import { cookies } from "next/headers";

const ACCEPTED_ADMIN_CODES = [
  "LD-ADMIN-2026",
  "ADMIN2026",
  "LORNETTE-ADMIN",
  "COACH2026",
  (process.env.FOUNDATIONS_ADMIN_CODE || "").trim().toUpperCase(),
].filter(Boolean);

export async function verifyAdminCodeAction(code: string) {
  const normalized = (code || "").trim().toUpperCase();

  if (!normalized) {
    return { success: false, message: "Please enter an admin access code." };
  }

  const isValid = ACCEPTED_ADMIN_CODES.includes(normalized);

  if (!isValid) {
    return {
      success: false,
      message: "Invalid admin access code. Please check your credentials or contact site administration.",
    };
  }

  // Set persistent admin access cookie
  const cookieStore = await cookies();
  cookieStore.set("ld_admin_access", "true", {
    path: "/",
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    maxAge: 60 * 60 * 24 * 30, // 30 days
  });

  return {
    success: true,
    message: "Admin code verified. Access granted to Performance Edge Golf workspace.",
    athleteId: "admin-coach-lornette",
  };
}

export async function createParticipantSessionAction(athleteId?: string) {
  const cookieStore = await cookies();
  cookieStore.set("ld_participant_access", athleteId || "participant", {
    path: "/",
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production",
    maxAge: 60 * 60 * 24 * 30, // 30 days
  });
  return { success: true };
}

export async function logoutFoundationsAction() {
  const cookieStore = await cookies();
  cookieStore.delete("ld_admin_access");
  cookieStore.delete("ld_participant_access");
  return { success: true };
}
