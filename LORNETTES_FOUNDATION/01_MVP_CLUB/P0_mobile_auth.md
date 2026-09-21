# Mobile Auth and Session Reliability

**Workstream:** 01_MVP_CLUB  
**Release:** Club MVP  
**Priority:** P0  
**Status:** DONE  
**Depends On:** NONE  
**Blocks:** 02_GOLF_V1_1  
**Source:** Simulated institutional stress test  

## Problem

Mobile participants frequently navigate between clubhouse Wi-Fi, weak cellular networks, mobile Safari background tabs, and their email application when authenticating via Magic Link. In early prototypes, session tokens dropped during 302 redirects, unhandled expired links left athletes on blank screens, and unauthenticated redirects risked open-redirect vulnerabilities.

## Why It Matters

If a high school golfer or amateur tournament competitor cannot reliably log in from their phone on the practice range, onboarding fails before the program begins. High friction at authentication causes immediate abandonment.

## Proposed Direction

Harden the passwordless authentication flow using current Next.js 16 and `@supabase/ssr` architecture:
1. Use `proxy.ts` (App Router middleware convention) to refresh tokens and propagate cookies across request and response headers.
2. Build a dedicated callback route (`src/app/auth/callback/route.ts`) implementing PKCE code exchange with explicit recovery for expired or already-used links.
3. Enforce an open-redirect defense sanitizing all `returnUrl` parameters to permitted `/foundations/*` application routes.
4. Support email OTP (6-digit code) as a reliable alternative when email apps open links in isolated in-app webviews.
5. Strictly exclude SMS and phone-number collection in this phase.

## Acceptance Criteria

- [x] Token refresh and cookie propagation handled centrally in Next.js 16 `proxy.ts`
- [x] Cookie `getAll` and `setAll` methods correctly synchronize `@supabase/ssr` cookies
- [x] Dedicated `/auth/callback` route executes PKCE exchange
- [x] Expired or reused magic links recover gracefully to login with clear error messaging
- [x] Open-redirect protection ensures `returnUrl` resolves only to relative `/foundations/*` routes
- [x] 6-digit email OTP supported as seamless alternative to Magic Link
- [x] Zero SMS or third-party phone dependencies introduced
- [x] Authenticated mobile users retain persistent sessions across browser backgrounding and foregrounding

## Non-Goals

- Adding SMS authentication, Twilio, or phone-number collection
- Adding social logins (Google, Apple, Facebook) in this release
- Offline biometric login (FaceID / TouchID)

## Evidence Needed

- Unit test verifying open-redirect sanitization, proxy matcher configuration, and PKCE exchange logic
- Production build confirming zero deprecated `@supabase/auth-helpers-nextjs` imports
- Mobile browser session testing

## Decision Notes

- **2026-09-17**: Simulation noted that mobile in-app browsers often drop session cookies on magic link redirects.
- **2026-09-17**: Decided against adding SMS (adds carrier cost, complexity, and compliance hurdles without necessity). Locked native Supabase passwordless (Magic Link + email OTP).
- **2026-09-17**: Implemented `src/proxy.ts` session refresh, `src/app/auth/callback/route.ts`, and sanitized return destinations. Verified 4/4 tests passing in `scripts/test-auth-hardening.mjs`.
