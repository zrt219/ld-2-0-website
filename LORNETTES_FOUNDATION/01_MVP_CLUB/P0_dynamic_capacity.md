# Database-Driven Dynamic Cohort Capacity

**Workstream:** 01_MVP_CLUB  
**Release:** Club MVP  
**Priority:** P0  
**Status:** DONE  
**Depends On:** NONE  
**Blocks:** 02_GOLF_V1_1  
**Source:** Simulated institutional stress test  

## Problem

Club dashboards historically used hard-coded default capacity states (such as `useState(12)`). When a club purchased an institutional license for 20 athletes, enrolling all 20 players displayed an impossible "167% activation" bug. Furthermore, registration routes did not enforce capacity limits transactionally on the server, risking over-enrollment races on the final available seat.

## Why It Matters

Head Professionals and Directors of Golf require accurate seat tracking and enrollment limits. Seeing inaccurate percentages damages credibility with institutional buyers, while over-enrolling beyond paid licenses creates operational disputes.

## Proposed Direction

Derive all capacity metrics directly from the database schema (`cohorts.capacity`, default 20, nullable for unlimited). Calculate enrolled counts, remaining spaces, and activation percentages dynamically. Enforce capacity limits transactionally on the server using PostgreSQL row-level locking (`FOR UPDATE`) in registration stored procedures.

## Acceptance Criteria

- [x] Capacity comes directly from database (`cohorts.capacity`)
- [x] Enrolled count comes directly from database
- [x] Remaining seats calculate accurately across 0, partial, full, and unlimited states
- [x] Impossible activation percentages (such as 167%) caused by stale UI defaults are eliminated
- [x] Server-side capacity enforcement blocks over-enrollment
- [x] Simultaneous final-seat redemption race conditions prevented via atomic database locks
- [x] Unlimited capacity (null) supported cleanly without calculation errors

## Non-Goals

- Building complex ticketing or tier-based variable pricing within the club dashboard
- Dynamic mid-cohort capacity downgrades below current enrolled counts

## Evidence Needed

- Unit test covering capacity calculations across 0, partial, full, over-capacity, and unlimited states
- Concurrency simulation on final-seat registration
- Schema migration verifying `cohorts.capacity` and stored procedure `register_cohort_athlete`

## Decision Notes

- **2026-09-17**: Simulation revealed 167% display bug when 20 juniors enrolled against hard-coded 12-seat state.
- **2026-09-17**: Added `capacity INTEGER DEFAULT 20` to `cohorts` table and created atomic `register_cohort_athlete` stored procedure with `FOR UPDATE` lock.
- **2026-09-17**: Updated `src/app/foundations/club/page.tsx` and `src/app/api/registration/route.ts`. Verified 8/8 tests passing in `scripts/test-capacity-and-roster.mjs`.
