# Rollback Strategy & Safeties

This document outlines the rollback and safety mechanisms for the current release.

## Database Rollback Strategy
Since we use Supabase, database rollbacks can be performed using migration down scripts. In the event of a breaking schema change:
1. Locate the migration file in `supabase/migrations/`
2. Run `supabase db reset` if in local development, or use the Supabase dashboard to restore from the automatic daily backup (Point-in-Time Recovery if enabled).
3. If specific tables need to be reverted, execute the down migrations manually.

## Deployment Rollback
Vercel is the primary deployment platform. To perform an instant rollback:
1. Open the Vercel Dashboard for the project.
2. Go to "Deployments".
3. Find the previous stable deployment.
4. Click the vertical dots (...) and select "Redeploy" or "Assign Custom Domain" to instantly point the production domain back to the previous build without waiting for a new build.

## Feature Flags & Disabled Systems
- **Email Sending (Resend)**: Currently, the real email delivery system in `/api/interest` is disabled for safety. It forces a `mailto:` fallback. To re-enable, remove the explicit `return NextResponse.json({ ok: false, fallbackRequired: true, message: ... })` early return.
- **Payments (Stripe)**: If `STRIPE_ENABLED` is set to `false`, the platform will not process live transactions and will use manual or test flow.
