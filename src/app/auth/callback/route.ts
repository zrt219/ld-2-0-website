import { NextResponse, type NextRequest } from "next/server";
import { cookies } from "next/headers";
import { createServerClient } from "@supabase/ssr";

function sanitizeReturnUrl(returnUrl: string | null): string {
  if (!returnUrl) return "/foundations/dashboard";

  // Prevent open redirect vulnerabilities: Must start with /foundations/ and not contain protocol or double slashes
  if (
    returnUrl.startsWith("/foundations/") &&
    !returnUrl.startsWith("//") &&
    !returnUrl.includes("://")
  ) {
    return returnUrl;
  }

  return "/foundations/dashboard";
}

export async function GET(request: NextRequest) {
  const requestUrl = new URL(request.url);
  const code = requestUrl.searchParams.get("code");
  const error = requestUrl.searchParams.get("error");
  const errorDescription = requestUrl.searchParams.get("error_description");
  const nextParam = requestUrl.searchParams.get("next") || requestUrl.searchParams.get("returnUrl");

  const destination = sanitizeReturnUrl(nextParam);

  // If Supabase returned an error in the callback URL (e.g. expired link, link already used)
  if (error || errorDescription) {
    const userFacingMsg = errorDescription?.includes("expired")
      ? "Your sign-in link has expired. Please request a new one."
      : "The authentication link is invalid or has already been used. Please sign in again.";

    return NextResponse.redirect(
      new URL(
        `/foundations/login?error=${encodeURIComponent(userFacingMsg)}&returnUrl=${encodeURIComponent(destination)}`,
        requestUrl.origin
      )
    );
  }

  // Handle PKCE Code exchange
  if (code) {
    const cookieStore = await cookies();
    const supabaseUrl = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
    const supabaseAnonKey = process.env.SUPABASE_ANON_KEY || process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

    if (!supabaseUrl || !supabaseAnonKey) {
      return NextResponse.redirect(
        new URL(
          `/foundations/login?error=${encodeURIComponent("Server configuration error. Please try again.")}`,
          requestUrl.origin
        )
      );
    }

    const response = NextResponse.redirect(new URL(destination, requestUrl.origin));

    const supabase = createServerClient(supabaseUrl, supabaseAnonKey, {
      cookies: {
        getAll() {
          return cookieStore.getAll();
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) => {
            try {
              cookieStore.set(name, value, options);
            } catch {}
            response.cookies.set(name, value, options);
          });
        },
      },
    });

    const { error: exchangeError } = await supabase.auth.exchangeCodeForSession(code);

    if (exchangeError) {
      console.warn("Auth exchangeCodeForSession failed:", exchangeError.message);
      return NextResponse.redirect(
        new URL(
          `/foundations/login?error=${encodeURIComponent("Sign-in link expired or already used. Please request a fresh link.")}&returnUrl=${encodeURIComponent(destination)}`,
          requestUrl.origin
        )
      );
    }

    // Successfully authenticated with cookies firmly set on response headers
    return response;
  }

  // If neither code nor error, check if user is already authenticated
  const cookieStore = await cookies();
  const supabaseUrl = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const supabaseAnonKey = process.env.SUPABASE_ANON_KEY || process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

  if (supabaseUrl && supabaseAnonKey) {
    const supabase = createServerClient(supabaseUrl, supabaseAnonKey, {
      cookies: {
        getAll() {
          return cookieStore.getAll();
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) =>
              cookieStore.set(name, value, options)
            );
          } catch {}
        },
      },
    });

    const {
      data: { user },
    } = await supabase.auth.getUser();

    if (user) {
      return NextResponse.redirect(new URL(destination, requestUrl.origin));
    }
  }

  // Default fallback: return to login cleanly
  return NextResponse.redirect(new URL("/foundations/login", requestUrl.origin));
}
