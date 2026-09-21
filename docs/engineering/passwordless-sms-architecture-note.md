# Architecture Note: Passwordless Email OTP vs. Future SMS Extension

Date: 2026-09-17
Status: Current lock: Email Magic Link & 6-Digit Email OTP only. SMS deferred.

## Current Architectural Decision
1. **Passwordless Foundation**:
   - Supabase Auth natively supports Magic Links and 6-digit email OTP through the same passwordless infrastructure.
   - Next.js 16 SSR cookie sessions are managed via `@supabase/ssr` with `proxy.ts` refreshing access tokens and propagating cookies.
   - Zero SMS provider dependencies (Twilio, MessageBird, etc.) are introduced in this pass, eliminating carrier delivery failures, international SMS roaming fees, and unnecessary telecom compliance overhead.

2. **Where SMS Can Be Added Later (If Real Pilot Data Demands It)**:
   - **Provider Integration Point**: Supabase native Twilio/MessageBird phone provider hook under `supabase.auth.signInWithOtp({ phone })`.
   - **Data Model**: Add `phone_number` and `phone_verified` columns to `profiles` with E.164 phone formatting (`zod` validation).
   - **UX Surface**: An alternate tab on `/foundations/login` alongside email entry.
   - **Triggers for Re-evaluating**:
     - Athlete pilot surveys indicating corporate or institutional email firewalls blocking magic link emails on golf course networks.
