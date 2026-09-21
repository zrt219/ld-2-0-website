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

  // Email sending is disabled for safety.
  // We force a fallback to mailto: link.
  return NextResponse.json({
    ok: false,
    fallbackRequired: true,
    message:
      "Email delivery is disabled. Please use the prepared mailto fallback.",
  });

  return NextResponse.json({
    ok: true,
    message:
      "Thank you for your interest. We’ll keep you informed as The Collection gets closer to launch.",
  });
}
