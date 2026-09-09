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
