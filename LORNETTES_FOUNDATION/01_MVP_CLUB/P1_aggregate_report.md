# Board-Ready Aggregate Cohort Report

**Workstream:** 01_MVP_CLUB  
**Release:** Club MVP  
**Priority:** P1  
**Status:** DONE  
**Depends On:** P0_dynamic_capacity, P0_roster_status  
**Blocks:** 02_GOLF_V1_1  
**Source:** Simulated institutional stress test  

## Problem

Directors of Golf, Academy Chairs, and Youth Committee Heads must justify program investments to their Board of Directors. Without an executive aggregate report, leadership cannot demonstrate participation, milestone completion, or program health without improperly sharing individual participant names and personal responses.

## Why It Matters

Institutional renewal decisions happen at the board and committee level. A clean, high-credibility executive summary ensures the club can review cohort performance, celebrate participation benchmarks, and authorize future seasonal cohorts.

## Proposed Direction

Create an ink-safe, board-ready aggregate report page at `/foundations/club/report` accessible from the club dashboard.
Include real aggregate data only:
- Club name, cohort title, dates, and program edition
- Real enrollment, activation percentage, and completion rates
- Week-by-week Foundation progression breakdown
- Small-cohort privacy suppression: automatically omit or group granular breakdowns when active cohort size is under 5 participants to prevent individual re-identification
- Print optimization: clean `@media print` layout, white background, ink-safe typography, page-break control, and "Print / Save PDF" action button.

## Acceptance Criteria

- [x] Dedicated `/foundations/club/report` route reachable via "View Cohort Report" button
- [x] Includes cohort name, dates, enrolled count, dynamic capacity, activation, and completion percentages
- [x] Displays Foundation milestone progression across all 10 canonical weeks
- [x] Small-cohort privacy protection suppresses granular subgroups for cohorts smaller than 5
- [x] Strictly zero raw reflection text, private triggers, or personal assessment answers
- [x] Zero fabricated scoring claims or unverified testimonials
- [x] Clean print-optimized layout (`@media print`) rendering perfectly on 8.5x11 letter paper
- [x] Includes generated date, reporting period, and program edition version stamp

## Non-Goals

- Integrating heavy server-side PDF generation binaries (e.g. Puppeteer) when browser-native print rendering produces superior vector quality
- In-app charting libraries that inflate client bundle size

## Evidence Needed

- Route availability test returning HTTP 200 at `/foundations/club/report`
- Print stylesheet audit confirming no severed containers or overflow clipping
- Small cohort privacy suppression test

## Decision Notes

- **2026-09-17**: Simulation indicated that golf committee chairs need a physical document to present at quarterly board meetings.
- **2026-09-17**: Built `src/app/foundations/club/report/page.tsx` with dedicated `@media print` CSS, dynamic search param reading (`?cohort=`), and small-cohort threshold protection. Verified HTTP 200 response on local production server.
