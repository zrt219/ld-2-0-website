# PGA / Club Coach Companion

**Workstream:** 01_MVP_CLUB  
**Release:** Club MVP  
**Priority:** P1  
**Status:** DONE  
**Depends On:** P0_roster_status  
**Blocks:** 02_GOLF_V1_1  
**Source:** Simulated institutional stress test  

## Problem

Athletes working with PGA technical swing coaches often experience conflicting instructions if their coach is unfamiliar with Lornette's mental performance concepts. Conversely, if a technical coach asks to read an athlete's personal reflections, the athlete's psychological safety is compromised.

## Why It Matters

Coaches are pivotal to an athlete's daily training environment. If the coach reinforces the same Performance Edge vocabulary (cadence, anchor cues, mistake reset), the athlete's progress accelerates dramatically. If the coach undermines it or violates privacy boundaries, the program stalls.

## Proposed Direction

Build a concise, club-facing PGA Coach Companion surface at `/foundations/club/coach-companion` summarizing, for each of the 10 Foundations:
1. Weekly Foundation title and theme
2. Relevant Performance Edge cue
3. What the coach should reinforce on the lesson tee
4. What the coach should avoid
5. Practical on-range drill or assignment
6. Explicit privacy reminder: never ask for or inspect private participant reflection text

Include support for a 20 to 30 minute Pre-Program PGA Coach Briefing checklist item within the cohort administration workflow.

## Acceptance Criteria

- [x] Dedicated Coach Companion page at `/foundations/club/coach-companion`
- [x] Canonical 10-Foundation weekly summary with cues, drills, and reinforcing language
- [x] Clear guidance on what coaches should avoid (e.g. over-analyzing misses right after poor shots)
- [x] Prominent Coach Privacy Boundary banner prohibiting inspection of athlete reflection text
- [x] Pre-Program Coach Briefing checklist module (20-30 min briefing status and schedule)
- [x] Print-friendly layout for distribution to academy staff

## Non-Goals

- Creating a separate, complex educational curriculum for coaches
- In-app video conferencing or live webinar hosting

## Evidence Needed

- Route availability test returning HTTP 200 at `/foundations/club/coach-companion`
- Verification of canonical 10-Foundation names and cues
- Privacy compliance audit

## Decision Notes

- **2026-09-17**: Simulation highlighted that swing instructors need practical on-range alignment without access to athletes' personal diary entries.
- **2026-09-17**: Built `src/app/foundations/club/coach-companion/page.tsx` covering all 10 Foundations with range cues and privacy walls. Verified HTTP 200 response on local production server.
