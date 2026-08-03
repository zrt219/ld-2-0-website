import { NextResponse } from "next/server";

import { inquirySchema } from "@/lib/inquiry-schema";

export async function POST(request: Request) {
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

  const resendKey = process.env.RESEND_API_KEY;
  const to = process.env.CONTACT_TO_EMAIL;

  if (!resendKey || !to) {
    return NextResponse.json({
      ok: false,
      fallbackRequired: true,
      message:
        "Email delivery is not configured. Please use the prepared mailto fallback.",
    });
  }

  const inquiry = parsed.data;

  if (inquiry.website) {
    return NextResponse.json({
      ok: true,
      message: "Inquiry received.",
    });
  }

  const text = [
    `Full name: ${inquiry.fullName}`,
    `Email: ${inquiry.email}`,
    `Phone: ${inquiry.phone || "Not provided"}`,
    `Organization: ${inquiry.organization}`,
    `Title / role: ${inquiry.role || "Not provided"}`,
    `Event type: ${inquiry.eventType}`,
    `Preferred date: ${inquiry.preferredDate || "Not provided"}`,
    `Alternate date: ${inquiry.alternateDate || "Not provided"}`,
    `Location type: ${inquiry.locationType}`,
    `City / venue: ${inquiry.cityVenue || "Not provided"}`,
    `Audience size: ${inquiry.expectedAudienceSize}`,
    `Budget range: ${inquiry.budgetRange || "Not provided"}`,
    `Topics: ${inquiry.topicsOfInterest.join(", ")}`,
    "",
    "Event goals:",
    inquiry.eventGoals,
  ].join("\n");

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      authorization: `Bearer ${resendKey}`,
      "content-type": "application/json",
    },
    body: JSON.stringify({
      from: process.env.CONTACT_FROM_EMAIL ?? "Lornette Daye Website <onboarding@resend.dev>",
      to,
      subject: `Booking inquiry for Lornette Daye: ${inquiry.eventType}`,
      text,
    }),
  });

  if (!response.ok) {
    return NextResponse.json(
      {
        ok: false,
        fallbackRequired: true,
        message:
          "Email delivery is temporarily unavailable. Please use the prepared mailto fallback.",
      },
      { status: 502 },
    );
  }

  return NextResponse.json({ ok: true, message: "Inquiry sent." });
}
