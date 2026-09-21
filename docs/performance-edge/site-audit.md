# Lornette Daye Website - Design Preservation & Performance Edge Site Audit

**Audit Date**: September 2026  
**Auditor**: Antigravity AI  
**Scope**: Pre-flight design, architecture, token, and routing audit for the *Performance Edge* expansion.

---

## 1. Current Stack & Architecture

* **Framework & Runtime**: Next.js 16.2.6 (App Router, Turbopack enabled, React 19.2.4, React DOM 19.2.4).
* **Language & Typing**: TypeScript 5.x (Strict mode, `tsconfig.json`).
* **Styling**: Tailwind CSS v4 (`@tailwindcss/postcss`, CSS variable `@theme inline` binding in `src/app/globals.css`).
* **Motion & Icons**: `framer-motion` 12.38.0, `lucide-react` 1.16.0.
* **Validation**: `zod` 4.4.3 (`inquiry-schema.ts`, `interest-schema.ts`).
* **Database & Auth SDK**: `@supabase/supabase-js`, `@supabase/ssr` (Next.js server & browser client utilities in `src/lib/supabase/`).
* **Deployment & Hosting**: Vercel (Production domain: `https://lornettedaye.com`).

---

## 2. Existing Reusable Components

The following existing components in `src/components/` must be reused to maintain visual continuity:

* **Layout & Navigation**:
  * [`PageShell.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/PageShell.tsx) - Standard page wrapper including skip link, header, main content anchor, footer, and mobile sticky CTA.
  * [`Header.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/Header.tsx) - Sticky header with monogram logo, desktop nav, and animated mobile accordion menu.
  * [`Footer.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/Footer.tsx) - Multi-column ivory/gold footer with legal, navigation, newsletter, and social links.
  * [`MobileStickyCTA.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/MobileStickyCTA.tsx) - Bottom fixed bar for small screens.
* **UI Blocks & Content Presenters**:
  * [`CTAButton.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/CTAButton.tsx) - Primary gold/ink and secondary bordered action buttons.
  * [`HeroSplit.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/HeroSplit.tsx) - Editorial split hero with high-res portrait and headline lockups.
  * [`SectionHeader.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/SectionHeader.tsx) - Centered or aligned section titles with eyebrow badges.
  * [`MetricStrip.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/MetricStrip.tsx) - Highlight stat counters (e.g. 40+ Years, Olympic Coach, 15+ Titles).
  * [`FAQAccordion.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/FAQAccordion.tsx) - Accessible expand/collapse question cards.
  * [`BookingForm.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/BookingForm.tsx) - Speaking / coaching booking form with validation.
  * [`TestimonialCard.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/TestimonialCard.tsx), [`TopicCard.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/TopicCard.tsx), [`VideoCard.tsx`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/components/VideoCard.tsx).

---

## 3. Existing Design Tokens & Visual Rules

Defined in [`src/app/globals.css`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/app/globals.css):

* **Color Palette**:
  * Background / Base: `--ivory: #faf7f0`
  * Card Surfaces: `--white: #ffffff`
  * Accent Champagne: `--champagne: #c6a55c`
  * Dark Gold / Text Accent: `--gold-dark: #7f5b1d`
  * Primary Typography: `--ink: #171412`
  * Subdued Text / Charcoal: `--charcoal: #2a2520`
  * Muted Taupe: `--taupe: #b7a891`
  * Borders & Dividing Rules: `--line: #e7dccb`, `--sand: #e8ddcb`, `#dfd1b4`
  * Focus Glow: `#f0cf7a` with 2px ink outline
* **Typography**:
  * Serif (Headings): `Playfair Display` (`var(--font-playfair)`)
  * Sans (Body & UI): `Inter` (`var(--font-inter)`)
* **Radii & Borders**:
  * Restrained rounded corners (`rounded-lg`, `rounded-xl`, `rounded-2xl` for cards; crisp borders with `#e7dccb` / `#dfd1b4`).

---

## 4. Navigation & Routing Conventions

* Current routes:
  * `/` (Home)
  * `/about` (Bio & Timeline)
  * `/speaking` (Keynotes, Topics, Inquiries)
  * `/leadership` (Executive Workshops)
  * `/mentorship` (Youth & Community)
  * `/athlete-coaching` (High Performance Athlete Mentorship)
  * `/programs` (Overview of offerings)
  * `/books` & `/book` (Digital Book Store)
  * `/collection` (The Collection waitlist)
  * `/media` & `/recognition` & `/impact` & `/events` & `/speaker-kit`
  * `/blog` & `/blog/[slug]` (Editorial insights)

---

## 5. Current Mobile Behavior & Accessibility

* Sticky top bar with custom burger menu (`data-mobile-menu-trigger`, `data-mobile-menu`).
* Fixed bottom sticky booking button on mobile viewport (`MobileStickyCTA.tsx`).
* Full WCAG 2.1 AA focus rings (`outline-offset: 4px`, `box-shadow: 0 0 0 4px #f0cf7a`).
* `prefers-reduced-motion` global suppression in CSS.

---

## 6. Existing Forms & Data Patterns

* **Speaking / Coaching Inquiry**: [`src/app/api/inquiry/route.ts`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/app/api/inquiry/route.ts)
* **The Collection Waitlist**: [`src/app/api/interest/route.ts`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/app/api/interest/route.ts)
* **Pattern**: Validated server route handlers with fallback mailto redirection if external keys are unconfigured.

---

## 7. Existing Supabase State

* **Connected Project**: `https://vbfddrqtgdbegtyvmmcp.supabase.co`
* **Clients**:
  * Browser: [`src/lib/supabase/client.ts`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/lib/supabase/client.ts)
  * Server (SSR): [`src/lib/supabase/server.ts`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/lib/supabase/server.ts)
  * Admin / Service Role: [`src/lib/supabase/admin.ts`](file:///c:/Users/Zhane/Documents/New%20project/LD%202.0%20WEBSITE/src/lib/supabase/admin.ts)
* **Vercel Production Env**: Configured with encrypted `SUPABASE_URL`, `SUPABASE_ANON_KEY`, and `SUPABASE_SERVICE_ROLE_KEY`.

---

## 8. Test & Deployment Setup

* `npm run build`: Next.js 16 App Router build (Turbopack).
* `npm run typecheck`: TypeScript strict check (`tsc --noEmit`).
* `npm run lint`: ESLint with Next.js rules.
* `npm run test:e2e`: Playwright E2E suite.

---

## 9. Performance Edge Visual Adaptations (Allowed)

* **Athletic Pacing**: High-impact athletic imagery with editorial luxury treatment.
* **Scorecard & Grid Accents**: Subtle gold-line scorecards, pillar grids, and workshop timelines.
* **Palette Continuity**: Must use standard `#faf7f0` ivory background, `#c6a55c` champagne, `#7f5b1d` dark gold, and `#171412` ink.
* **Pillars & Metrics**: 8 Golf Performance pillars rendered in existing `TopicCard` or elevated gold-bordered card structures.

---

## 10. Explicit DO-NOT-CHANGE List

1. **Brand Identity**: Do NOT change Lornette Daye's monogram logo, brand name, or primary color tokens.
2. **Global Navigation**: Do NOT remove or break existing top-level links (`/`, `/about`, `/speaking`, `/books`, `/media`, etc.).
3. **Core Copy Tone**: Maintain Lornette Daye's authoritative Olympian voice (40+ years Olympic coach & national champion).
4. **Credential Integrity**: Never describe Lornette as a clinical psychologist or therapist. Use *Performance Coaching, Mental Game, Athlete Mindset, Focus, Resilience, Pressure Management*.

---

## 11. Risks & Conflicts to Avoid

* **Parallel Design Systems**: Do not install separate UI component libraries (e.g. Shadcn/Chakra) that conflict with the Tailwind v4 token system.
* **Broken Routing**: Ensure all new Performance Edge routes live cleanly under `/performance` or `/performance-edge` without overwriting existing `/programs` or `/athlete-coaching`.
* **Client Leak of Service Keys**: Ensure `SUPABASE_SERVICE_ROLE_KEY` is never referenced in Client Components (`"use client"`).

---

## 12. Canonical Route Map for Foundations & Golf V1

*(Note: Supersedes earlier exploratory draft route proposals under `/performance`. Canonical architecture is locked in `GOLF_V1_CANONICAL_PRODUCT_SPEC.md`)*

* `/foundations` - Main Lornette’s Foundation Landing
* `/foundations/golf` - Flagship Golf Pathway (10 Athletic Foundations & Performance Edge Framework)
* `/foundations/golf/keynote` - Keynote: Playing Your Best When It Matters (60–90 min)
* `/foundations/golf/workshop` - Golf Performance Workshop & Member Clinic (~2 hours)
* `/foundations/golf/program` - Lornette’s Foundation — Golf (10-Week Guided Program)
* `/foundations/golf/club-partnership` - Private Club Partnership & Proposal Page
* `/foundations/clubs` - For Clubs & Teams Institutional Partnerships
* `/foundations/performance-edge` - The Performance Edge Framework (8 Practical Performance Tools)
* `/foundations/dashboard` (with compatibility redirect from `/performance/dashboard`) - Athlete Member Portal (Prompts 12–19)
* `/foundations/admin` (with compatibility redirect from `/performance/admin`) - Protected Admin Portal (Prompt 11)
