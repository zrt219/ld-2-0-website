<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.

## Next.js 16 Server Action & Boundary Invariants

1. **Dedicated Actions File Only (`actions.ts`)**:
   - Never declare inline `"use server"` functions inside Page or Layout components (`page.tsx` or `layout.tsx`).
   - Always extract Server Actions into a dedicated `actions.ts` file marked with `"use server"` at the very top.
   - Server-only modules (`next/headers`, `next/cache`, `revalidatePath`, `cookies()`) must only be imported into `actions.ts` or standalone server utilities, never mixed into modules consumed by client trees.

2. **Local Hosting & Dev Server Verification**:
   - When requested to host or test locally, always check for stale processes occupying port 3000 (`Get-NetTCPConnection -LocalPort 3000`) before launching.
   - Prefer `npx next start -p 3000` (production mode) after running `npm run build` to verify genuine production runtime behavior and avoid Next.js 16 Webpack-vs-Turbopack dev mode discrepancies.
<!-- END:nextjs-agent-rules -->

<!-- BEGIN:buffer-publishing-rules -->
# Buffer & Social Media Campaign Invariants

1. **Mandatory Visual Assets & Production Custom Domain Invariant**:
   - Every scheduled social post (LinkedIn, etc.) must include a valid, high-resolution visual asset. Never schedule or queue text-only posts unless explicitly instructed by the user.
   - **Production Custom Domain Only**: Never pass Vercel preview/hash URLs (`*-zrt219s-projects.vercel.app`) to Buffer (`createPost`), as Vercel preview protection blocks Buffer's media scraper. All media assets must be served from `https://lornettedaye.com/campaigns/...` and return `HTTP 200`.
2. **Pre-Flight Asset Deployment & Zero-404 Invariant**:
   - Before calling the Buffer API, ensure all local images and videos are added to git, committed, and pushed to remote origin.
   - Run production deployment (`vercel --prod`) and probe every target URL via automated HTTP GET/HEAD on `https://lornettedaye.com`.
   - **Hard Invariant**: If any media asset returns non-200 or is missing from production, HALT scheduling immediately until the asset is live.
3. **Queue vs. Drafts vs. Ideas Transparency**:
   - By default, campaign scheduling adds posts directly to the channel's **Scheduled Queue / Calendar** (`saveToDraft: false`, `mode: "customScheduled"`) for automated hands-free publishing.
   - When communicating status to users, clearly report where posts reside in the Buffer UI (Channel -> Queue/Calendar vs. Drafts vs. Ideas) so users know exactly where to locate them.
   - If draft staging is explicitly requested, use `saveToDraft: true` / `createContentItemDraft`.
4. **Automated Error Self-Healing & Media Fallback Protocol**:
   - For any posts in Buffer that encounter posting errors (e.g., LinkedIn media URL rejection), run automated self-healing via `editPost` GraphQL mutation with verified CDN URLs.
   - Maintain persistent queue tracking in `scripts/master-campaign-queue.json` and execution reports in `scripts/scheduled-master-report.json`.
5. **100% Autonomous Background Timer & Power-Off Fallback Protocol**:
   - When batch-scheduling posts, if a daily API limit (e.g. 24h window), channel limit, or queue threshold is reached:
     - **Never** leave unscheduled posts as a manual follow-up or reminder for the user.
     - **Immediately** generate a dedicated recovery script (`scripts/schedule-master.mjs`) and persistent queue JSON (`scripts/master-campaign-queue.json`).
     - **Autonomously** register a background timer (`schedule` tool with `TimerCondition="never"`).
     - **Power-Off & Reboot Fallback (Self-Healing)**: All queue progress is persisted to `scripts/scheduled-master-report.json`. Upon session re-engagement or computer startup, the agent must automatically check for pending/overdue queue items and run catchup execution (`node scripts/schedule-master.mjs --catchup`) without requiring user prompts.
     - **Zero User Interventions**: Confirm to the user that execution is 100% autonomous, resilient to system restarts, and self-healing.
6. **Maximized Visibility & Conversion**: Include rich, pain-point-driven copy in Lornette Daye's authoritative voice (40+ years Olympian coach & national champion), an exhaustive hashtag stack for platform discoverability, and clear calls-to-action to `https://lornettedaye.com`.
<!-- END:buffer-publishing-rules -->

<!-- BEGIN:lornette-daye-book-catalog -->
# Lornette Daye Official Book Catalog & CTA Invariants

All published digital editions are priced at **$14.99 CAD**. When composing social media ad copy, campaign CTAs, or website content, dynamically align post themes to the relevant book from this canonical catalog:

1. **Survival Skills for Men** ($14.99 CAD)
   - *Subtitle*: Build resilience, balance, and purpose in every part of your life.
   - *Description*: A comprehensive guide for men who want to strengthen emotional resilience, clarify purpose, and build steadier daily habits through seasons of pressure and transition.
   - *Best For*: Men seeking clarity and practical strategies to navigate pressure, stress, and leadership with confidence.
   - *Core Pillars*: Resilience & balance, Purpose-centered reflection, Practical growth prompts.
   - *Stripe Link*: `https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00`

2. **Finish Strong: Chasing the Olympic Dream** ($14.99 CAD)
   - *Subtitle*: A journey of resilience, purpose, and legacy.
   - *Description*: A motivational autobiography drawn from Lornette's elite-athlete lens, focused on perseverance, identity, discipline, and rising again after setbacks.
   - *Best For*: Aspiring athletes, coaches, youth leaders, and anyone driven to achieve ambitious goals.
   - *Core Pillars*: Elite athlete mindset, Resilience after pressure, Purpose and legacy.
   - *Stripe Link*: `https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A`

3. **Surviving Life** ($14.99 CAD)
   - *Subtitle*: A guide to finding strength, embracing purpose, and living with hope.
   - *Description*: A warm, encouraging guide for readers rebuilding hope, confidence, and perspective after difficult seasons.
   - *Best For*: Individuals, women's groups, mentoring circles, faith communities, and anyone seeking practical encouragement.
   - *Core Pillars*: Hope after hardship, Resilience practices, Confidence and renewal.
   - *Stripe Link*: `https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02`

4. **Survival Skills for Athletes** ($14.99 CAD)
   - *Subtitle*: A guide to promote focus and excellence in every stage of life.
   - *Description*: A comprehensive resource for athletes at every level who want to build focus, resilience, discipline, and a champion mindset on and off the field.
   - *Best For*: Athletes, coaches, sports teams, youth leaders, and anyone competing in sport or in life.
   - *Core Pillars*: Champion mindset building, Focus & discipline on and off the field, Resilience through setbacks & pressure.
   - *Stripe Link*: `https://buy.stripe.com/PLACEHOLDER_ATHLETES` (or `https://lornettedaye.com/books`)

5. **Survival Skills for Believers** ($14.99 CAD)
   - *Subtitle*: A Christian guide to living with wisdom, grace, and peace.
   - *Description*: A faith-based guide helping believers navigate life's hardest chapters with purpose, scripture-backed wisdom, and the confidence that comes from knowing your identity in Christ.
   - *Best For*: Christians, faith communities, church groups, and anyone who wants to deepen their walk while navigating real-world challenges.
   - *Core Pillars*: Faith-centered resilience, Scripture-backed wisdom for hard seasons, Peace & purpose in every stage of life.
   - *Stripe Link*: `https://buy.stripe.com/PLACEHOLDER_BELIEVERS` (or `https://lornettedaye.com/books`)

6. **Survival Skills for Women** ($14.99 CAD)
   - *Subtitle*: A comprehensive guide to living with hope, resilience, and meaning.
   - *Description*: A warm, practical guide for women who want to rebuild confidence, discover purpose, and thrive through every season — from pressure and loss to growth and renewal.
   - *Best For*: Women, women's groups, mentoring circles, faith communities, and anyone navigating personal growth and transformation.
   - *Core Pillars*: Confidence & identity restoration, Hope & healing after hard seasons, Practical tools for thriving with meaning.
   - *Stripe Link*: `https://buy.stripe.com/PLACEHOLDER_WOMEN` (or `https://lornettedaye.com/books`)

7. **UMATTR Devotional** ($14.99 CAD)
   - *Subtitle*: Reflections for the moments that ask you to keep going.
   - *Description*: A devotional journal for anyone who needs a reminder that they matter — featuring reflective prompts, encouragement, and truth to hold onto when life gets heavy.
   - *Best For*: Students, athletes, individuals in transition, faith communities, and anyone who needs a daily anchor of hope and worth.
   - *Core Pillars*: Daily reflections to anchor your worth, Prompts for hope in hard moments, Faith-based encouragement to keep going.
   - *Stripe Link*: `https://buy.stripe.com/PLACEHOLDER_UMATTR` (or `https://lornettedaye.com/books`)

8. **Survival Skills for Students** ($14.99 CAD)
   - *Subtitle*: Practical tools for focus, balance, and success at every stage.
   - *Description*: A student-centered guide packed with strategies for managing academic pressure, building healthy habits, and staying grounded in purpose through the demands of school and life.
   - *Best For*: Students, parents, educators, mentors, and youth leaders who want to support young people in building focus and resilience.
   - *Core Pillars*: Academic pressure management, Balance & healthy habits for students, Purpose & resilience through school life.
   - *Stripe Link*: `https://buy.stripe.com/PLACEHOLDER_STUDENTS` (or `https://lornettedaye.com/books`)

9. **Survival Skills: Surviving to Thriving** ($14.99 CAD)
   - *Subtitle*: The journey from just getting by to truly living.
   - *Description*: A transformational guide that takes readers beyond survival mode — helping them identify what's holding them back, rebuild their foundation, and step into a life of genuine purpose and momentum.
   - *Best For*: Anyone feeling stuck, overwhelmed, or ready to move beyond surviving and into a life that truly thrives.
   - *Core Pillars*: Moving beyond survival mode, Purpose-driven momentum, Rebuilding your foundation for real growth.
   - *Stripe Link*: `https://buy.stripe.com/PLACEHOLDER_SURVIVING_TO_THRIVING` (or `https://lornettedaye.com/books`)
<!-- END:lornette-daye-book-catalog -->

<!-- BEGIN:performance-edge-golf-v1 -->
# Repository Agent Context — Performance Edge
The authoritative Performance Edge planning/build system and product files live in:
`Lornette_Daye_Performance_Edge_Launch3_Prompt_Pack/`

Treat that directory as the SINGLE SOURCE OF TRUTH for all Performance Edge Golf V1 prompts, product locks, participant flow, security contracts, acceptance criteria, and execution instructions.

Do not silently override those files with stale prompts, mockup copy, code comments, or implementation convenience.

Preserve and extend the existing LornetteDaye.com design.

Execute the numbered Performance Edge build plan one prompt at a time.
<!-- END:performance-edge-golf-v1 -->

<!-- BEGIN:visual-framing-and-editorial-plaque-rules -->
# Visual Asset Framing Calibration & Docked Luxury Editorial Plaque Invariants

1. **Docked Luxury Editorial Plaque Invariant**:
   - All Foundations hero cards and photographic feature overlays must present captions within the standardized Docked Luxury Editorial Plaque:
     ```tsx
     <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
       <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
         {eyebrow}
       </p>
       <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
         {title}
       </p>
     </div>
     ```
   - No floating disconnected island badges inside image boundaries. The plaque must anchor flush to the bottom edge (`inset-x-0 bottom-0`).
   - No raw gradients that allow text to bleed directly onto white attire, greens, or sunlit architectural elements.

2. **Aspect-Ratio Focal Calibration Invariant**:
   - Every 16:9 image displayed in a vertical frame (`aspect-[4/5]`) must have its subject center visually verified.
   - Set optical `objectPosition` coordinates specifically to center the subject and preserve full facial, gesture, and equipment visibility.
<!-- END:visual-framing-and-editorial-plaque-rules -->

<!-- BEGIN:foundations-10-week-canonical-invariants -->
# Lornette's Foundation — Golf 10-Week Canonical Invariants

1. **Strict 10-Week / 10-Foundation Architecture**:
   - The canonical Golf program is **Lornette's Foundation — Golf: 10-Week Guided Athlete Development Program**.
   - Curriculum consists of exactly **10 Athletic Foundations**:
     1. Identity Beyond Sport
     2. Champion Mindset
     3. Discipline Systems
     4. Resilience After Setback
     5. Pressure, Emotional Regulation & Recovery
     6. Communication & Presence
     7. Family & Community Support
     8. Career & Money Readiness
     9. Personal Brand & Story
     10. Legacy & Community Impact
   - Prohibited obsolete claims: `4-week Golf program`, `4-week guided program`, `8-pillar Golf program`, `8-module Golf program`, `8/8 program completion`.

2. **Performance Edge Framework Separation**:
   - The Performance Edge Framework is a methodology/tooling layer (Focus, Pre-Shot Routine, Pressure, Visualization, Reset, Decision-Making, Competition Preparation, Confidence).
   - Performance Edge tools are mapped across the 10 Foundation weeks; they do not dictate module counts or duration.

3. **LMS & Learner Dashboard State Contracts**:
   - Progress must always display `Week X of 10` and `X of 10 Foundations Complete`.
   - Domain and database models must support ordered weeks and flexible activity counts per week.
   - Learner LMS implementation remains paused until canonical 10-week multimedia asset production is reconciled.
<!-- END:foundations-10-week-canonical-invariants -->

<!-- BEGIN:public-asset-and-opengraph-invariants -->
# Public Asset Hygiene & Production OpenGraph Invariants

1. **Zero-Bloat Public Asset Invariant**:
   - The `public/` directory must only contain actively used, referenced web assets.
   - Never commit raw AI generation batches, uncompressed iterations, unreferenced video clips, or temporary archives (`.zip`, `.csv`, `.docx`) into `public/`.
   - Cleaned product images must reside in `public/products/clean/`.
   - All uncurated or exploratory generation artifacts must remain in scratch/archive storage outside `public/`.

2. **Production OpenGraph Verification**:
   - All social metadata (`metadata.openGraph.images` and `metadata.twitter.images` in `src/app/layout.tsx`) must resolve to a valid file on disk.
   - The canonical executive portrait is located at `/generated/lornette-executive-portrait.jpg`.
   - Never reference `/images/lornette-executive-portrait.jpg` (non-existent).
<!-- END:public-asset-and-opengraph-invariants -->

<!-- BEGIN:learner-portal-visual-lock -->
# Learner Portal & Course Player Visual System Lock

1. **Brand Hierarchy & Naming Invariant**:
   - Canonical program brand: **Lornette’s Foundation — Golf**.
   - Subordinate methodology line: **Powered by the Performance Edge Framework**.
   - Private golfer workspace: **My Performance Edge** / **Welcome to My Performance Edge**.
   - Prohibited program heading: `The Performance Edge — Golf`.

2. **Left Sidebar Atmospheric Device**:
   - The desktop learner sidebar must retain a scenic golf image container in the lower portion of the rail.
   - Must feature the signature Lornette principle: *“Your previous shot cannot hit your next shot.”*
   - Must present the luxury motto: *BETTER PEOPLE · BETTER PLAYERS*.
   - Purely decorative images must maintain `alt=""` for assistive technology compliance.

3. **Weekly Athlete Reflection Structure**:
   - Reflection cards in the course player must explicitly support the three canonical prompt dimensions:
     1. *What did you notice?*
     2. *What worked?*
     3. *What will you repeat?*
   - Responses are strictly private to the participant and reviewed by Coach Lornette Daye.
<!-- END:learner-portal-visual-lock -->

<!-- BEGIN:brand-voice-and-copy-invariants -->
# Lornette Daye Brand Voice & Editorial Copy Invariants

1. **Authoritative, Dignified Olympian Voice**:
   - Lornette Daye is a 40+ year Olympic-level coach and Canadian national champion. Her brand tone is dignified, authoritative, calm, and grounded in athletic excellence, discipline, and emotional poise.
   - **Strictly Prohibited**:
     - Crude, negative, or fear-based sales hooks (e.g., *"Stop choking"*, *"Choking under pressure"*, *"Collapse on the back nine"*, *"Your worst enemy stands between your ears"*).
     - Aggressive internet-marketer hype, bro-coaching clichés, or melodramatic combativeness.
     - Clinical or psychological diagnostic framing.
   - **Canonical & Approved Phrasing**:
     - *"Playing Your Best When It Matters."*
     - *"The mental side of golf performance, focus under pressure, and repeatable execution."*
     - *"Better People · Better Players."*
     - *"Your previous shot cannot hit your next shot."*
2. **Zero Unapproved Headline Inventions**:
   - Never invent ad-hoc hero headlines, hooks, or taglines when working on Performance Edge / Foundations pages.
   - All page titles, headlines, subtitles, and badges MUST directly derive from the canonical prompt pack (`Lornette_Daye_Performance_Edge_Launch3_Prompt_Pack/`) and `GOLF_V1_TERMINOLOGY_GUARD.md`.
3. **Strict No Em Dash Invariant ("—")**:
   - **Never** use em dashes (`—`, `&mdash;`, or `\u2014`) in any ad copy, headlines, paragraphs, captions, or editorial text.
   - Use clean, standard punctuation instead: periods for distinct thoughts, commas for parentheticals/clauses, colons for introductions, or restructure into clear, standalone sentences.
<!-- END:brand-voice-and-copy-invariants -->

<!-- BEGIN:canonical-monogram-logo-invariant -->
# Canonical Monogram Logo Invariant

1. **Mandatory Brand Logo Asset**:
   - The official, canonical brand logo across the entire site is strictly `/monogramlogo.png` (the authentic cursive "LD" monogram).
   - Never replace, swap, or alter this asset with square badge icons, generic typography, or alternate files (such as `/images/ld-official-gold-logo.png`).
   - This invariant applies universally to:
     1. Main Website Header (`src/components/Header.tsx`)
     2. Learner Portal Header (`src/components/foundations/learner/LearnerHeader.tsx`)
     3. Learner Mobile Drawer (`src/components/foundations/learner/LearnerShell.tsx`)
     4. Foundations Dashboard Hero Banner (`src/app/foundations/dashboard/page.tsx`)
2. **Rendering & Aspect Ratio Invariant**:
   - Because `/monogramlogo.png` is an authentic wide-format signature monogram, always render it with `object-contain`, `unoptimized`, and calibrated width-to-height proportions to preserve legibility without distortion.
   - **Main Website Header (`src/components/Header.tsx`) Sizing Lock**:
     - Desktop (`sm:` and above): Monogram `h-[66px] w-auto max-w-[118px]`, divider `h-11 w-px bg-[#d9c69e]`, brand name `sm:text-[1.62rem]`, tagline `text-[0.66rem] tracking-[0.24em] mt-1`.
     - Mobile (`< sm`): Monogram `h-[58px] w-auto max-w-[104px]`, brand name `text-[1.35rem]`.
     - Nav Container: Always maintain `h-[94px]` to provide balanced vertical breathing room and proper alignment for desktop nav links and the mobile menu toggle. Never shrink below `94px`.
   - **Learner Portal / Dashboard Headers**: Keep compact dashboard sizing (`h-9 sm:h-11 w-12 sm:w-14 shrink-0`).
<!-- END:canonical-monogram-logo-invariant -->

<!-- BEGIN:panoramic-cta-and-react19-invariants -->
# Panoramic CTA Banner & React 19 State Invariants

1. **Panoramic Scenic Closing CTA Invariant**:
   - Every closing CTA section on Foundations, Golf, and program landing pages must use a full-bleed panoramic scenic background image (`relative overflow-hidden min-h-[340px] sm:min-h-[400px] border-t border-[rgba(198,165,92,0.4)]`).
   - Must include an atmospheric darkening gradient overlay (`bg-gradient-to-t from-black/85 via-black/60 to-black/75`), Champagne uppercase eyebrow (`text-[var(--champagne)]`), white serif heading, and gold CTA buttons.
   - Never leave raw flat black/white container backgrounds on signature bottom closing CTAs.

2. **React 19 / Next.js State Sync Guardrail**:
   - Never invoke `setState` synchronously within a `useEffect` body to synchronize external store data or prop updates.
   - For custom external or localStorage stores, always use React's `useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot)` with stable cached module snapshots.
   - For resetting internal form state on active record/item switches, adjust state during render (`if (prevId !== currentId) { setPrevId(currentId); ... }`) or use React `key={activeId}` remounting.
<!-- END:panoramic-cta-and-react19-invariants -->

<!-- BEGIN:luxury-navigation-and-cta-invariants -->
# Luxury Navigation Scrollbar & CTA Icon Invariants

1. **Zero Visible Scrollbar Tracks on Navigation Rails & Drawers**:
   - Every scrollable navigation component (including desktop sidebar `<aside>`, sticky rail wrappers, mobile drawer contents, and horizontal tab bars) must apply the `.no-scrollbar` utility class:
     ```tsx
     className="overflow-y-auto no-scrollbar"
     ```
   - Standardize cross-browser scrollbar suppression in `globals.css`:
     ```css
     .no-scrollbar::-webkit-scrollbar { display: none; }
     .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
     ```
   - Touch scrolling and mousewheel interactions must remain 100% functional.

2. **Single Clean Icon Formatting on CTA Buttons**:
   - `CTAButton` automatically appends an `<ArrowUpRight />` icon when `showIcon={true}` (the default).
   - Never embed literal arrow symbols (`→`, `&rarr;`, `↗`, `&nearr;`) within the children text string passed to `<CTAButton>`.
   - If a directional arrow is already rendered by the component, use clean, punchy text only:
     - **Incorrect**: `<CTAButton href="...">EXPLORE THE ATHLETE PROGRAM &rarr;</CTAButton>`
     - **Correct**: `<CTAButton href="...">EXPLORE THE ATHLETE PROGRAM</CTAButton>`
<!-- END:luxury-navigation-and-cta-invariants -->

<!-- BEGIN:foundations-admin-and-portal-auth-invariants -->
# Foundations Portal, Admin Console & Dual-Auth Invariants

1. **Dual-Layer Authentication Architecture**:
   - Protected routes (`/foundations/dashboard`, `/foundations/admin`, `/foundations/lessons`, `/foundations/plan`, `/foundations/club`, `/foundations/account`) must support dual authentication:
     a) Active Supabase Auth session (`user.id` + `profiles.is_admin`), OR
     b) Verified administrative cookie (`ld_admin_access=true`) established via accepted admin access codes.
   - Canonical Admin Codes: `LD-ADMIN-2026`, `ADMIN2026`, `LORNETTE-ADMIN`, `COACH2026`, and `process.env.FOUNDATIONS_ADMIN_CODE`.
   - Never remove or override cookie-based admin verification in `src/proxy.ts`, `src/app/foundations/admin/page.tsx`, or `src/app/foundations/login/actions.ts`.

2. **Zero-404 Redirection Invariant**:
   - Unauthenticated access to any protected `/foundations/*` route must redirect to `/foundations/login?returnUrl=...`.
   - Never redirect unauthenticated users to `/login` (non-existent route).
   - Sanitize `returnUrl` to prevent self-referencing redirect loops.

3. **Offline & Empty-Table Resilient Fallback Data**:
   - All 6 Admin Console tabs (`inquiries`, `participants`, `cohorts`, `enrollments`, `plans`, `resources`) must provide rich, production-grade fallback mock data (`FALLBACK_INQUIRIES`, `FALLBACK_COHORTS`, etc.) whenever Supabase tables are unseeded, empty, or offline.
   - Admin pages must never crash with unhandled exceptions when database queries fail.

4. **Dedicated Server Action Files**:
   - All server actions must reside in dedicated `actions.ts` files (`src/app/foundations/login/actions.ts`, `src/app/foundations/admin/actions.ts`) with `"use server"` declared at the top of the file.
   - Never declare inline `"use server"` functions inside page or layout components.

5. **Luxury Error Boundary Invariant**:
   - All foundations routes must be protected by Next.js error boundaries (`src/app/foundations/error.tsx` and `src/app/foundations/admin/error.tsx`).
   - Error boundaries must adhere to the luxury visual system (onyx background `#120f0d`, champagne accents, gold borders, `/monogramlogo.png`, retry action, and return to dashboard).

6. **Environment-Bound Test Runner Security**:
   - Test runner bypasses (e.g. `x-playwright-test` header) must strictly be conditioned on `process.env.NODE_ENV !== "production"`.
   - Never allow User-Agent or header spoofing to bypass authentication in production.

7. **Strict Admin Code Confidentiality & Zero-Public-Exposure Invariant**:
   - Never print, echo, or expose the specific administrative access code string publicly in chat responses, documentation, error messages, user-facing UI copy, input placeholders, or help text.
   - Always refer to administrative credentials generically in communication (e.g., *"the authorized administrative access code"* or *"the configured administrative access key"*).
   - In `src/app/foundations/login/page.tsx`:
     - **Zero Pre-fill**: The admin code input must initialize to an empty string (`""`) and never be pre-filled with secret code values by default.
     - **Generic Placeholders**: The admin code input placeholder must remain a generic `"Enter Admin Access Key"`.
     - **Clean Cohort Inputs**: The registration cohort code input placeholder must never mention or hint at the admin code.
     - **No Public Hint Text**: Never render plain-text helper copy stating default or fallback admin credentials.
<!-- END:foundations-admin-and-portal-auth-invariants -->

<!-- BEGIN:lornettes-foundation-product-backlog -->
# Lornette's Foundation Canonical Product Roadmap & Backlog

For Lornette's Foundation roadmap questions, read:
`LORNETTES_FOUNDATION/README.md`
and the relevant workstream README:

1. `01_MVP_CLUB/` = Current first-club product hardening
2. `02_GOLF_V1_1/` = Active next-iteration Golf backlog
3. `03_ITALY_FIG/` = Institutional research backlog

Invariants:
- Never move an Italy item into MVP merely because it appears important.
- Requirements from `03_ITALY_FIG` must never be used to block or expand the First Club MVP.
- Simulated stress test feedback must be clearly labeled as `Source: Simulated institutional stress test` until validated by real user data.
<!-- END:lornettes-foundation-product-backlog -->
