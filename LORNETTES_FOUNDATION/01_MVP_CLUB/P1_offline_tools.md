# Fast-Access On-Course Field Tools

**Workstream:** 01_MVP_CLUB  
**Release:** Club MVP  
**Priority:** P1  
**Status:** DONE  
**Depends On:** P0_autosave  
**Blocks:** 02_GOLF_V1_1  
**Source:** Simulated institutional stress test  

## Problem

The highest-value psychological tools (5-Second Mistake Reset, Pre-Shot Routine, Pressure Plan) are needed directly on the golf course or practice range where cellular connectivity is weak. Having to navigate through multiple levels of LMS video lessons to review a routine is impractical during active play.

## Why It Matters

Athletic performance edge tools only work if they can be retrieved in the critical 15 to 30 seconds before a shot or immediately after a double-bogey. If the tool is inaccessible or requires heavy video loading, golfers will not use it in competition.

## Proposed Direction

Add a dedicated, lightweight Quick Tools surface accessible within 1 to 2 taps from the learner header and navigation drawer (`/foundations/quick-tools`).
Include canonical tools:
- 5-Second Mistake Reset (Acknowledge, Evaluate, Release, Reset, Recommit; "Your previous shot cannot hit your next shot.")
- 6-Step Pre-Shot Routine
- Pressure Plan & Physiological Sigh
- Focus / Anchor Cue

Design for mobile outdoor readability: large high-contrast typography, minimal decorative UI, ink-safe print layout, and zero requirement for typing or private data entry. Provide a clear "Print / Save to Device" path using standard browser capabilities without forcing a complex PWA dependency.

## Acceptance Criteria

- [x] Dedicated `/foundations/quick-tools` page accessible in 1 click from header and drawer
- [x] Canonical 5-Step Mistake Reset sequence accurately presented with Lornette's signature principle
- [x] 6-Step Pre-Shot Routine clearly structured for on-course pacing
- [x] Physiological sigh breathing cadence and heart-rate recovery guide included
- [x] High-contrast, outdoor-readable visual presentation
- [x] Print / Save PDF styling works cleanly via `@media print`
- [x] Zero typing required and zero private reflection data exposed
- [x] Fast load time with zero heavy multimedia dependencies

## Non-Goals

- Building a heavy Progressive Web App (PWA) with service-worker cache bust complexities
- Live biometric sensor integration or GPS rangefinder features

## Evidence Needed

- Route availability test returning HTTP 200 at `/foundations/quick-tools`
- Visual inspection under outdoor high-contrast styling
- Print stylesheet verification

## Decision Notes

- **2026-09-17**: Simulation confirmed golfers cannot navigate LMS video players while walking down the fairway.
- **2026-09-17**: Decided to build a lightweight, dedicated Quick Tools route rather than adding an unneeded heavy PWA framework.
- **2026-09-17**: Created `src/app/foundations/quick-tools/page.tsx`, added quick triggers to `LearnerHeader.tsx`, and verified HTTP 200 response on local production server.
