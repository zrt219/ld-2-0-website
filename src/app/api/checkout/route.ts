import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { cohortCode, fullName, email, clubCode } = body;

    if (!email || !fullName) {
      return NextResponse.json(
        { error: "Full name and email are required." },
        { status: 400 }
      );
    }

    // 1. Club-Funded / Partner Code Bypass (Prompt 23 invariant)
    if (clubCode) {
      const validClubCodes = ["DERRICK-FALL-2026", "CAPILANO-FALL-2026", "STGEORGE-2026"];
      if (validClubCodes.includes(clubCode.trim().toUpperCase())) {
        return NextResponse.json({
          success: true,
          type: "club_sponsored",
          message: "Club partnership verified. Workspace unlocked.",
          redirectUrl: "/foundations/dashboard",
        });
      }
    }

    // 2. Direct Individual Checkout Feature Flag
    const isDirectCheckoutEnabled = process.env.NEXT_PUBLIC_ENABLE_DIRECT_CHECKOUT === "true";
    const stripeSecretKey = process.env.STRIPE_SECRET_KEY;

    if (!isDirectCheckoutEnabled || !stripeSecretKey) {
      // Inquiry fallback / demo enrollment confirmation
      return NextResponse.json({
        success: true,
        type: "individual_inquiry",
        message: "Registration request recorded. Our team will issue your cohort access key.",
        redirectUrl: "/foundations/dashboard",
      });
    }

    // 3. Dependency-free Stripe Checkout Session via Stripe REST API
    const host = req.headers.get("host") || "lornettedaye.com";
    const protocol = host.includes("localhost") ? "http" : "https";

    const params = new URLSearchParams();
    params.append("mode", "payment");
    params.append("customer_email", email);
    params.append("payment_method_types[0]", "card");
    params.append("line_items[0][price_data][currency]", "cad");
    params.append("line_items[0][price_data][product_data][name]", "Lornette’s Foundation: Golf 10-Week Guided Cohort");
    params.append("line_items[0][price_data][product_data][description]", "Full 10-week guided athlete development program, weekly Lornette sessions, and Performance Edge plan review.");
    params.append("line_items[0][price_data][unit_amount]", "149900");
    params.append("line_items[0][quantity]", "1");
    params.append("metadata[cohortCode]", cohortCode || "GOLF-FALL-2026");
    params.append("metadata[fullName]", fullName);
    params.append("success_url", `${protocol}://${host}/foundations/dashboard?checkout=success&session_id={CHECKOUT_SESSION_ID}`);
    params.append("cancel_url", `${protocol}://${host}/foundations/golf/program?checkout=cancelled`);

    const stripeRes = await fetch("https://api.stripe.com/v1/checkout/sessions", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${stripeSecretKey}`,
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: params.toString(),
    });

    const sessionData = await stripeRes.json();

    if (!stripeRes.ok) {
      throw new Error(sessionData.error?.message || "Failed to create Stripe checkout session");
    }

    return NextResponse.json({
      success: true,
      type: "stripe_checkout",
      url: sessionData.url,
    });
  } catch (error: unknown) {
    console.error("Checkout API error:", error);
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Internal checkout error" },
      { status: 500 }
    );
  }
}
