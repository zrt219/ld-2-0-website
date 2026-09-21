/* eslint-disable @typescript-eslint/no-explicit-any */
import { NextResponse } from "next/server";
import Stripe from "stripe";
import { createAdminClient } from "@/lib/supabase/admin";
import { apiRateLimit } from "@/lib/rate-limit";

export const dynamic = "force-dynamic";

// Feature flag check
const ENABLE_PAYMENTS = process.env.NEXT_PUBLIC_ENABLE_PAYMENTS === "true";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || "sk_test_dummy", {
  apiVersion: "2024-06-20" as any,
});

export async function POST(request: Request) {
  const ip = request.headers.get("x-forwarded-for") || "unknown";
  if (apiRateLimit.isRateLimited(ip)) {
    return NextResponse.json({ ok: false, message: "Too many requests" }, { status: 429 });
  }

  if (!ENABLE_PAYMENTS) {
    return NextResponse.json({ ok: false, message: "Payments are currently disabled." }, { status: 403 });
  }

  try {
    const { registrationId, email } = await request.json();

    if (!registrationId || !email) {
      return NextResponse.json({ ok: false, message: "Missing registration ID or email." }, { status: 400 });
    }

    const supabase = createAdminClient();
    
    // Verify registration exists and is individual_paid
    const { data: reg, error } = await supabase
      .from("registrations")
      .select("id, registration_type, status")
      .eq("id", registrationId)
      .eq("email", email)
      .single();

    if (error || !reg) {
      return NextResponse.json({ ok: false, message: "Registration not found." }, { status: 404 });
    }

    if (reg.registration_type !== "individual_paid") {
      return NextResponse.json({ ok: false, message: "This registration does not require payment." }, { status: 400 });
    }

    if (reg.status === "paid") {
      return NextResponse.json({ ok: false, message: "Registration is already paid." }, { status: 400 });
    }

    // Create checkout session
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ["card"],
      line_items: [
        {
          price: process.env.STRIPE_PRICE_ID || "price_dummy",
          quantity: 1,
        },
      ],
      mode: "payment",
      success_url: `${process.env.NEXT_PUBLIC_SITE_URL}/foundations/login?payment=success`,
      cancel_url: `${process.env.NEXT_PUBLIC_SITE_URL}/foundations/register?payment=cancelled`,
      client_reference_id: registrationId,
      customer_email: email,
    });

    return NextResponse.json({ ok: true, url: session.url });
  } catch (err: any) {
    console.error("Stripe checkout error:", err);
    return NextResponse.json({ ok: false, message: "Failed to create checkout session." }, { status: 500 });
  }
}
