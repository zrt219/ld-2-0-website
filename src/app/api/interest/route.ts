import { NextResponse } from "next/server";

import { interestSchema } from "@/lib/interest-schema";

export async function POST(request: Request) {
  const body = await request.json().catch(() => null);
  const parsed = interestSchema.safeParse(body);

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

  const data = parsed.data;

  // Honeypot spam check
  if (data.website) {
    return NextResponse.json({
      ok: true,
      message: "Thank you for your interest. We'll keep you informed as The Collection gets closer to launch.",
    });
  }

  const text = [
    "New Collection Interest List Sign-Up",
    "------------------------------------",
    `First Name: ${data.firstName}`,
    `Email: ${data.email}`,
    `Product Interests: ${data.interests.join(", ")}`,
    data.notes ? `Notes / Reference: ${data.notes}` : "",
  ]
    .filter(Boolean)
    .join("\n");

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      authorization: `Bearer ${resendKey}`,
      "content-type": "application/json",
    },
    body: JSON.stringify({
      from:
        process.env.CONTACT_FROM_EMAIL ??
        "Lornette Daye Collection <onboarding@resend.dev>",
      to,
      subject: `The Collection Interest List: ${data.firstName} (${data.interests.join(", ")})`,
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

  return NextResponse.json({
    ok: true,
    message:
      "Thank you for your interest. We’ll keep you informed as The Collection gets closer to launch.",
  });
}
