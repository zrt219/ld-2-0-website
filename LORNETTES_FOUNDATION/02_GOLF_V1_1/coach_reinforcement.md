# Advanced Coach Reinforcement Engine

**Workstream:** 02_GOLF_V1_1  
**Release:** Golf V1.1  
**Priority:** V1.1 (Priority 4)  
**Status:** BACKLOG  
**Depends On:** 01_MVP_CLUB, variable_cadence  
**Blocks:** NONE  
**Source:** Product decision  

## Problem

While the P1 Coach Companion provides static weekly cues and range drills, high-performance golf academies frequently ask for structured lesson-plan integration. Coaches want prompt ideas for 45-minute private lessons that reinforce that week's Foundation without asking athletes to show them their personal written reflections.

## Why It Matters

When private swing instructors and mental performance programs pull athletes in opposite directions, the golfer suffers. Structuring intentional touchpoints for the coach strengthens the athlete's support team while maintaining an ironclad privacy wall.

## Proposed Direction

Expand the Coach Companion into a structured reinforcement engine:
- Printable or exportable weekly 1-page lesson integration guides
- 5-minute pre-lesson check-in cues (e.g. "What was your focus cue this week?")
- Post-round debriefing frameworks for coaches (focusing on composure and decision-making instead of raw scores)
- Shared vocabulary reference cards for academy coaching staffs

Strict Privacy Boundary:
Coaches will never be given access to raw participant reflection text, private assessment responses, or Lornette's personal review notes. The reinforcement engine operates entirely on outward cues and practice design.

## Acceptance Criteria

- [ ] 10-week lesson plan alignment guides produced for coaches
- [ ] Explicit coach debrief prompt sequences that steer away from score criticism
- [ ] Strict privacy architecture maintained; zero participant diary access
- [ ] Tested with at least two PGA academy directors for ease of integration
- [ ] Mobile-friendly printable format available in the club portal

## Non-Goals

- Building video swing analysis or multi-angle stroke capture tools
- Allowing technical coaches to grade or approve mental reflections

## Evidence Needed

- Direct feedback from academy coaches during Club MVP pilot delivery
- Documented coach demand for structured drill sequences

## Decision Notes

- **2026-09-17**: Logged in Golf V1.1 backlog. Implementation deferred until Club MVP pilot generates live coaching feedback.
