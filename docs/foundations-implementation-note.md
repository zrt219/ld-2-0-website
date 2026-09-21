# Implementation Note: Adding Foundations to LornetteDaye.com

**Date**: 2026-09-17  
**Scope**: Natural extension of the existing Lornette Daye visual system to include "Lornette's Foundation" and its sub-pathways without redesigning existing pages.

---

## 1. Files and Components to Reuse
- **Page Layout**: `src/components/PageShell.tsx` (provides skip-to-content, global `Header`, `main-content` landmark, `Footer`, and `MobileStickyCTA`).
- **Typography & Brand**: Headings in `font-serif` (`Playfair Display`), body & UI in `font-sans` (`Inter`), loaded via `src/app/layout.tsx`.
- **Buttons & CTAs**: `src/components/CTAButton.tsx` (`primary`, `secondary`, `dark` variants).
- **Headers & Labels**: `src/components/SectionHeader.tsx`, SectionLabel pattern (`text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]`).
- **Media & Cards**: `src/components/VideoCard.tsx`, `src/components/TopicCard.tsx`, `src/components/TestimonialCard.tsx`.
- **Images**: Existing portrait assets and verified brand imagery from `src/content/site.ts` and `public/images/`.

## 2. Nav Component Location & Changes
- **Location**: `src/components/Header.tsx`.
- **Desktop Navigation**:
  - Insert `Foundations` immediately after `Speaker`.
  - Dropdown under `Foundations`:
    - Lornette's Foundation (`/foundations`)
    - Golf (`/foundations/golf`)
    - For Clubs & Teams (`/foundations/clubs`)
    - Performance Edge Framework (`/foundations/performance-edge`)
  - Dropdown under `Books`:
    - Books (`/books`)
    - Collection (`/collection`)
  - Order: Home, Speaker, Foundations, Leadership, Mentorship, Books, About, Media, Blog.
  - Active State: Reuse existing thin gold underline (`border-b-2 border-[var(--gold-dark)] text-[var(--gold-dark)]`).
  - Accessibility: Full keyboard support (Enter/Space to toggle, Escape to close, arrow navigation, `aria-expanded`, `aria-haspopup`, outside click handler).
- **Mobile Navigation**:
  - Seamless disclosure for `Foundations` and `Books`.
  - Touch target size ≥ 44px (`min-h-11`).
  - Animated with Framer Motion, matching existing mobile drawer.

## 3. Current Design Tokens
- `--ivory`: `#faf7f0` (default background)
- `--white`: `#ffffff`
- `--champagne`: `#c6a55c` (accents & dividers)
- `--gold-dark`: `#7f5b1d` (active states, gold labels)
- `--ink`: `#171412` (dark text, dark backgrounds)
- `--charcoal`: `#2a2520` (subtle body text)
- `--taupe`: `#b7a891`
- `--sand`: `#e8ddcb`
- `--line`: `#e7dccb` (thin borders)

## 4. Route Structure to Implement
- `/foundations` — Main athlete development overview landing page.
- `/foundations/golf` — Flagship golf performance pathway page.
- `/foundations/clubs` — B2B club, academy, and team partnerships page.
- `/foundations/performance-edge` — The Performance Edge methodology and framework page.
- Secondary Sub-Navigation: Rendered on all `/foundations*` pages directly beneath the primary header.

## 5. Responsive Behavior
- Desktop: Max-width 7xl (`1280px`), horizontal flex nav with dropdown menus on click/hover/keyboard focus.
- Tablet (768px–1024px): Responsive wrapping, clean grid collapse.
- Mobile (< 768px): Hamburger trigger, full-width slide-down drawer with nested sub-menus. No horizontal overflow.
