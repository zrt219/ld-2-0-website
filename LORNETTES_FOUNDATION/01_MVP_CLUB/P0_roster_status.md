# Club Operational Roster and Zero Data Bleed

**Workstream:** 01_MVP_CLUB  
**Release:** Club MVP  
**Priority:** P0  
**Status:** DONE  
**Depends On:** P0_dynamic_capacity  
**Blocks:** 02_GOLF_V1_1  
**Source:** Simulated institutional stress test  

## Problem

Club leadership needs to know who has redeemed cohort invitations, who is actively engaging, and who has completed the program. However, without a dedicated operational roster, staff cannot verify participation without risking exposure of deeply private athlete reflections, personal triggers, and assessment answers.

## Why It Matters

Coaching staff and administrators need operational clarity to manage cohort rollouts. However, athlete trust depends on complete psychological safety. If an athlete suspects their head professional or parents can read their mistake reflections or emotional vulnerability entries, they will write superficial answers or refuse to participate.

## Proposed Direction

Add an operational roster table in the club dashboard showing operational identity only: participant name, invited email, status (`INVITED`, `REGISTERED`, `ACTIVE`, `COMPLETED`, `INACTIVE`), current Foundation week, and completion status. Enforce strict database RLS policies and query boundaries so club administrators cannot query raw reflection text or assessment responses.

## Acceptance Criteria

- [x] Operational roster table integrated into `/foundations/club`
- [x] Displays operational identity: name, email, status, current Foundation, completed count
- [x] Operational filtering supported: All, Pending, Active, Completed
- [x] Strict zero data bleed: raw reflection text is never included in roster queries
- [x] Private assessment answers and Lornette review notes remain strictly hidden from club admins
- [x] Database RLS prevents club admins from querying private participant data even via API
- [x] Real completion counts verified against database progress instead of fabricated estimates

## Non-Goals

- Building a bloated enterprise CRM with messaging, marketing campaigns, or contact history
- Realtime WebSocket streaming for simple roster updates (standard page refreshes suffice)

## Evidence Needed

- RLS test confirming club admin query returns 0 rows or errors when attempting to read reflections
- Roster filtering and state calculation tests
- Operational roster UI inspection

## Decision Notes

- **2026-09-17**: Simulation highlighted tension between coach administration and athlete privacy.
- **2026-09-17**: Defined strict privacy boundary: operational tracking is allowed; psychological content is prohibited.
- **2026-09-17**: Added `get_club_operational_roster` RPC in migration `20260918000000_club_mvp_hardening.sql`. Integrated operational table with status filters into `src/app/foundations/club/page.tsx`. Verified 8/8 tests passing in `scripts/test-capacity-and-roster.mjs`.
