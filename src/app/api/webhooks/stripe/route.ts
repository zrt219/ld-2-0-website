import { NextRequest, NextResponse } from "next/server";
import crypto from "crypto";

export async function POST(req: NextRequest) {
  try {
    const signature = req.headers.get("stripe-signature");
    const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;

    if (!signature || !webhookSecret) {
      return NextResponse.json(
        { message: "Stripe webhook acknowledged (unconfigured environment mode)" },
        { status: 200 }
      );
    }

    const rawBody = await req.text();

    // Verify Stripe signature header using HMAC SHA-256
    const sigElements = signature.split(",").reduce((acc: Record<string, string>, item) => {
      const [key, value] = item.split("=");
      if (key && value) acc[key.trim()] = value.trim();
      return acc;
    }, {});

    const timestamp = sigElements["t"];
    const expectedSig = sigElements["v1"];

    if (!timestamp || !expectedSig) {
      return NextResponse.json({ error: "Malformed signature" }, { status: 400 });
    }

    const signedPayload = `${timestamp}.${rawBody}`;
    const computedSig = crypto
      .createHmac("sha256", webhookSecret)
      .update(signedPayload, "utf8")
      .digest("hex");

    if (computedSig !== expectedSig) {
      console.error("Stripe signature mismatch");
      return NextResponse.json({ error: "Invalid signature" }, { status: 400 });
    }

    const event = JSON.parse(rawBody);

    if (event.type === "checkout.session.completed") {
      const session = event.data?.object;
      const { cohortCode, fullName } = session?.metadata || {};
      const customerEmail = session?.customer_email;

      console.info(
        `[STRIPE FULFILLMENT] Enrolled ${fullName} (${customerEmail}) into cohort ${cohortCode}`
      );
    }

    return NextResponse.json({ received: true });
  } catch (error: unknown) {
    console.error("Stripe webhook error:", error);
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Webhook processing error" },
      { status: 500 }
    );
  }
}
