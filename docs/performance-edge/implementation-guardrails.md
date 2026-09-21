# Lornette Daye Performance Edge - Implementation Guardrails

These guardrails MUST be reviewed prior to executing any subsequent Performance Edge prompts (Prompts 02 through 26).

---

## 1. Visual & Design System Invariants

1. **Color Tokens**:
   - Use CSS variables: `var(--ivory)`, `var(--champagne)`, `var(--gold-dark)`, `var(--ink)`, `var(--taupe)`, `var(--line)`.
   - Never introduce unaligned bright blues, purples, or generic SaaS neon accents.
2. **Typography**:
   - Editorial headlines: `font-serif` (`Playfair Display`).
   - Body & UI: `font-sans` (`Inter`).
3. **Component Reusability**:
   - Wrap new public routes in `<PageShell>` to maintain global header, footer, accessibility landmarks, and mobile CTA bars.
   - Use `<CTAButton>` and `<SectionHeader>` for all section introductions.

---

## 2. Content & Brand Authenticity Invariants

1. **Voice & Authority**:
   - Lornette Daye: 40+ years Olympic coach, national champion, executive mentor.
   - Core pillars: Focus, emotional reset, pre-shot routines, mistake recovery, competition preparation.
2. **Medical & Psychological Language Prohibition**:
   - Never describe Lornette as a clinical psychologist, psychotherapist, or medical practitioner.
   - Terminology: *Performance Coach, Mental Game Specialist, Mindset Strategist, Pressure Management Guide*.
3. **Zero Fabricated Proof**:
   - Do not invent fake partner logos, fake player testimonials, or fictional club endorsements. Use verified copy or neutral placeholders.

---

## 3. Architecture & Supabase Invariants

1. **Route Namespace**:
   - All Performance Edge routes live under `/performance/*` or `/api/performance/*`.
   - Existing marketing routes (`/`, `/about`, `/speaking`, `/books`, `/media`) remain untouched.
2. **Security & Key Isolation**:
   - `SUPABASE_SERVICE_ROLE_KEY` must NEVER be exposed in client bundles (`"use client"`).
   - All database tables must have **Row Level Security (RLS)** enabled from initial migration.
3. **Dependency Discipline**:
   - Do NOT install heavy external UI frameworks. Utilize Tailwind CSS v4, `framer-motion`, and `lucide-react`.

---

## 4. Verification Checklist (Post-Prompt Standard)

Before concluding any prompt:
- [ ] `npm run typecheck` passes with 0 errors.
- [ ] `npm run build` generates all static and dynamic routes cleanly.
- [ ] Mobile responsive layout verified.
- [ ] WCAG 2.1 AA accessibility (focus visible, skip link, contrast) intact.
