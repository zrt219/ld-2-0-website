<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

<!-- BEGIN:buffer-publishing-rules -->
# Buffer & Social Media Campaign Invariants

1. **Mandatory Visual Assets**: Every scheduled social post (LinkedIn, etc.) must include a valid, high-resolution image asset. Never schedule or queue text-only posts unless explicitly instructed by the user.
2. **Pre-Flight Asset Deployment & Validation**: Before calling the Buffer API, ensure all local images are committed, pushed, and deployed to production (e.g. Vercel), and verify each URL returns `HTTP 200` with an image MIME type.
3. **100% Autonomous Background Timer Protocol**:
   - When batch-scheduling posts, if a daily API limit (e.g. 24h window), channel limit, or queue threshold is reached:
     - **Never** leave unscheduled posts as a manual follow-up or reminder for the user.
     - **Immediately** generate a dedicated recovery script (e.g. `scripts/schedule-*-remaining.mjs`).
     - **Autonomously** register a background timer (`schedule` tool with `TimerCondition="never"` or appropriate condition) to wake up and dispatch the remaining queue as soon as the window clears.
     - Confirm to the user that execution is fully autonomous and hands-free.
4. **Maximized Visibility & Conversion**: Include rich, pain-point-driven copy in Lornette Daye's authoritative voice (40+ years Olympian coach & national champion), an exhaustive hashtag stack for platform discoverability, and clear calls-to-action to `https://lornettedaye.com`.
<!-- END:buffer-publishing-rules -->
