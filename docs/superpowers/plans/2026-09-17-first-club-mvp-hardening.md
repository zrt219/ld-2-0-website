# First Real Club MVP Hardening: P0 + P1 Implementation Plan

Date: 2026-09-17
Product: Lornette's Foundation - Golf
Scope: P0 + P1 Operational Hardening

## Architectural Invariants
- 10-Week / 10-Foundation Golf V1 canonical architecture intact
- Strict No Em Dash invariant across all customer and partner text
- Next.js 16 dedicated Server Actions files (`actions.ts`) with top-level `"use server"`
- Cookie-based sessions with `@supabase/ssr` and `proxy.ts`
- Privacy boundary: Club admins NEVER have access to private participant reflections, assessments, or personal performance plans
- No SMS, no real outbound emails during automated runs (two-step approval required)
- No Italian / FIG compliance scope; no Golf V1.1 scope

---

## Task Breakdown

### TASK 1: Reflection Draft Resilience (P0)
- [x] Implement robust client-side reflection draft layer in `src/lib/foundations/offline-store.ts`
  - Namespaced keying: `foundation-draft:${userId}:${cohortOrEnrollmentId}:${lessonId}`
  - IndexedDB storage with localStorage fallback
  - Debounced autosave (500-1000ms after typing stops)
  - Subtle status feedback: "Draft saved on this device", "Saving...", "Saved", "Offline - draft protected"
  - Server save remains authoritative; draft deleted on successful save
  - Purge draft on explicit save, account change/logout, or discard
- [x] Connect draft layer to `src/app/foundations/lessons/page.tsx`
- [x] Verify test cases: connection lost, app backgrounding, reload restore, network fail recovery, success deletion

### TASK 2: Dynamic Cohort Capacity (P0)
- [x] Add canonical database schema support for `cohorts.capacity` (default 20, nullable for unlimited)
- [x] Update `src/app/foundations/club/page.tsx` to read dynamic capacity from database (eliminate hard-coded `useState(12)`)
- [x] Enforce server-side transactional capacity validation in registration / cohort redemption (`src/app/api/registration/route.ts` and store/actions)
- [x] Support capacity states: 0 enrolled, partial, full (20/20), over-enrollment guard, unlimited (null)
- [x] Prevent race conditions on last available seat

### TASK 3: Club Roster / Operational View (P0)
- [x] Add operational roster table in `src/app/foundations/club/page.tsx`
- [x] Display operational identity only: participant name, email, enrollment status (INVITED, REGISTERED, ACTIVE, COMPLETED, INACTIVE), current Foundation/week, completion status
- [x] Strict RLS/query privacy guarantee: zero access to reflections, assessments, plans, or Lornette reviews
- [x] Add operational filtering: All, Pending, Active, Completed

### TASK 4: Mobile Auth / Session Reliability (P0)
- [x] Audit and update `src/proxy.ts` for Next.js 16 and `@supabase/ssr`
  - Correct redirect to `/foundations/login` with safe `returnUrl`
  - Token refresh and cookie propagation on request/response
- [x] Create auth callback route `src/app/auth/callback/route.ts` with PKCE exchange
- [x] Graceful mobile recovery handling: expired link, used link, invalid callback, background/foreground transition
- [x] Open redirect defense: sanitize return destinations to `/foundations/*`

### TASK 5: Passwordless Fallback UX (P1)
- [x] Update `/foundations/login` with clear passwordless choices:
  - Magic link (primary)
  - 6-digit email OTP (secondary fallback)
- [x] Email delivery UX: show email used, change email, resend countdown, spam/junk notice
- [x] Email safety: zero real outbound emails sent during testing (local/mock auth safe)
- [x] Add engineering documentation on why SMS is omitted and where it could plug in later

### TASK 6: Fast / Offline Golf Field Tools (P1)
- [x] Add dedicated Quick Tools surface accessible within 1-2 interactions (`/foundations/quick-tools` and header/drawer access)
- [x] Core approved tools:
  - 5-Second Reset Card (Acknowledge, Evaluate, Release, Reset, Recommit; "Your previous shot cannot hit your next shot.")
  - 6-Step Pre-Shot Routine
  - Pressure Plan & Physiological Sigh
  - Focus / Anchor Cue
- [x] Mobile outdoor readability: large high-contrast text, minimal decoration, zero typing required, zero private data exposed
- [x] Device-friendly caching / print & save offline path

### TASK 7: PGA / Club Coach Companion (P1)
- [x] Create PGA Club Coach Companion surface in `/foundations/club/coach-companion/page.tsx` or `/foundations/club`
- [x] Compact 10-week Foundation summary: weekly Foundation, Performance Edge cue, what to reinforce, what to avoid, on-range application
- [x] Explicit coach privacy rule: do not request private reflection/assessment data
- [x] Cohort pre-program briefing checklist item (20-30 min briefing date, status, notes)

### TASK 8: Board-Ready Aggregate Report (P1)
- [x] Create board-ready aggregate cohort report (`/foundations/club/report`)
- [x] Clean print-optimized layout (`@media print`, ink-safe, white background, no cutoffs)
- [x] Real aggregate metrics only: cohort title, dates, capacity, enrolled, activation %, completion %, foundation progress
- [x] Small cohort privacy suppression (if cohort < 5)
- [x] CTA in club dashboard: "VIEW COHORT REPORT" and "PRINT / SAVE PDF"

### TASK 9: P0/P1 Integration QA & Verification
- [x] Security regression: participant isolation, club admin restricted from reflections/assessments
- [x] End-to-end simulation across all 20 steps (verified via `scripts/test-club-mvp-e2e.mjs`)
- [x] Mobile viewport checks (360x800, 375x812, 390x844, 412x915, 430x932, tablet, desktop)
- [x] Run test suite, Playwright, typecheck, lint, build, Golf V1 verifier
- [x] Create backlog files: `docs/product/golf-v1-1-backlog.md` and `docs/product/italy-fig-backlog.md`
- [x] Final comprehensive report and CLUB MVP P0/P1 READY verdict
