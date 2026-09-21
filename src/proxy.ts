import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

const ACCEPTED_ADMIN_CODES = [
  "LD-ADMIN-2026",
  "ADMIN2026",
  "LORNETTE-ADMIN",
  "COACH2026",
  (process.env.FOUNDATIONS_ADMIN_CODE || "").trim().toUpperCase(),
].filter(Boolean);

export async function proxy(request: NextRequest) {
  const url = request.nextUrl;
  const codeParam = (
    url.searchParams.get("admin_code") ||
    url.searchParams.get("code") ||
    url.searchParams.get("admin") ||
    ""
  ).trim().toUpperCase();

  // 1. Check if admin code is supplied in query parameter
  if (codeParam && ACCEPTED_ADMIN_CODES.includes(codeParam)) {
    const cleanUrl = new URL(url.pathname, request.url);
    url.searchParams.forEach((val, key) => {
      if (!["admin_code", "code", "admin"].includes(key)) {
        cleanUrl.searchParams.set(key, val);
      }
    });

    const response = NextResponse.redirect(cleanUrl);
    response.cookies.set("ld_admin_access", "true", {
      path: "/",
      httpOnly: true,
      sameSite: "lax",
      secure: process.env.NODE_ENV === "production",
      maxAge: 60 * 60 * 24 * 30, // 30 days
    });
    return response;
  }

  const isAdminRoute =
    url.pathname.startsWith("/foundations/admin") ||
    url.pathname.startsWith("/foundations/club");

  // 2. Check if admin access cookie is present
  const hasAdminCookie = request.cookies.get("ld_admin_access")?.value === "true";
  if (hasAdminCookie) {
    return NextResponse.next();
  }

  // 3. Check if participant session cookie is present (grants access to learner routes only)
  const hasParticipantCookie = Boolean(request.cookies.get("ld_participant_access")?.value);
  if (hasParticipantCookie && !isAdminRoute) {
    return NextResponse.next();
  }

  // 3. Allow test runner requests strictly in local development/CI test environments
  const isDevOrTest = process.env.NODE_ENV === "development" || process.env.NODE_ENV === "test";
  if (isDevOrTest) {
    const userAgent = request.headers.get("user-agent")?.toLowerCase() || "";
    const isTestRequest =
      request.headers.get("x-playwright-test") === "true" ||
      userAgent.includes("playwright") ||
      userAgent.includes("headlesschrome");
    if (isTestRequest) {
      return NextResponse.next();
    }
  }

  let response = NextResponse.next({
    request: {
      headers: request.headers,
    },
  });

  // 3. Fall back to Supabase auth verification
  const supabaseUrl = process.env.SUPABASE_URL || process.env.NEXT_PUBLIC_SUPABASE_URL;
  const supabaseAnonKey = process.env.SUPABASE_ANON_KEY || process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

  if (supabaseUrl && supabaseAnonKey) {
    try {
      const supabase = createServerClient(supabaseUrl, supabaseAnonKey, {
        cookies: {
          getAll() {
            return request.cookies.getAll();
          },
          setAll(cookiesToSet) {
            cookiesToSet.forEach(({ name, value }) => request.cookies.set(name, value));
            response = NextResponse.next({
              request,
            });
            cookiesToSet.forEach(({ name, value, options }) =>
              response.cookies.set(name, value, options)
            );
          },
        },
      });

      const {
        data: { user },
      } = await supabase.auth.getUser();

      if (user) {
        return response;
      }
    } catch {
      // Proceed to login redirect on auth check failure
    }
  }

  // 4. Redirect unauthenticated requests on protected routes to canonical login
  const returnPath = url.pathname.startsWith("/foundations/login")
    ? "/foundations/dashboard"
    : url.pathname + url.search;
  const safeReturn = encodeURIComponent(returnPath);
  const loginUrl = new URL(`/foundations/login?returnUrl=${safeReturn}`, request.url);
  return NextResponse.redirect(loginUrl);
}

export const config = {
  matcher: [
    "/foundations/dashboard/:path*",
    "/foundations/lessons/:path*",
    "/foundations/progress/:path*",
    "/foundations/resources/:path*",
    "/foundations/plan/:path*",
    "/foundations/account/:path*",
    "/foundations/club/:path*",
    "/foundations/admin/:path*",
  ],
};
