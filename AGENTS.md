<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
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
