/* eslint-disable @typescript-eslint/no-explicit-any */
import { NextResponse } from "next/server";
import Stripe from "stripe";
import { createAdminClient } from "@/lib/supabase/admin";

export const dynamic = "force-dynamic";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || "sk_test_dummy", {
  apiVersion: "2024-06-20" as any,
});

const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET || "";

export async function POST(request: Request) {
  // If Stripe is not enabled or webhook secret is unconfigured, return 200 to prevent noisy errors
  if (!process.env.NEXT_PUBLIC_STRIPE_ENABLED || !process.env.STRIPE_WEBHOOK_SECRET) {
    return NextResponse.json({ ok: true, message: "Stripe disabled or unconfigured in this environment" }, { status: 200 });
  }

  const body = await request.text();
  const sig = request.headers.get("stripe-signature");

  let event: Stripe.Event;

  try {
    if (!sig) throw new Error("Missing stripe signature");
    event = stripe.webhooks.constructEvent(body, sig, webhookSecret);
  } catch (err: any) {
    console.error(`Webhook Error: ${err.message}`);
    return NextResponse.json({ error: `Webhook Error: ${err.message}` }, { status: 400 });
  }

  // Idempotent fulfillment
  if (event.type === "checkout.session.completed") {
    const session = event.data.object as Stripe.Checkout.Session;
    const registrationId = session.client_reference_id;

    if (registrationId) {
      const supabase = createAdminClient();
      
      const { error } = await supabase
        .from("registrations")
        .update({ status: "paid" })
        .eq("id", registrationId)
        .eq("status", "pending"); // ensure idempotency (only update if pending)

      if (error) {
        console.error("Error updating registration status:", error);
        return NextResponse.json({ error: "Database error" }, { status: 500 });
      }
    }
  }

  return NextResponse.json({ received: true });
}
