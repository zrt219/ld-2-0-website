# Variable Pre-Shot Routine Cadence

**Workstream:** 02_GOLF_V1_1  
**Release:** Golf V1.1  
**Priority:** V1.1 (Priority 3)  
**Status:** DISCOVERY_COMPLETE  
**Depends On:** 01_MVP_CLUB  
**Blocks:** NONE  
**Source:** Simulated institutional stress test  

## Problem

The canonical 6-step pre-shot routine in Foundation 3 provides essential structural consistency. However, on-course conditions vary dramatically: severe crosswinds, difficult lies, rain delays, or playing in fast pairings. A single rigid 18-second timing expectation can cause players to rush or over-think when conditions require quick triggers or deliberate resets.

## Why It Matters

Elite competitive golf requires disciplined adaptability. When a player is forced to back off due to a gusting crosswind or crowd movement, knowing how to reset the cadence without carrying tension into the swing is the difference between a pure strike and a pulled hook.

## Proposed Direction

Explore three situational cadence adaptations that build upon the core 6-step routine architecture:
1. **Standard Cadence (Full Routine)**: 14 to 18 seconds. Normal fairway approach or tee shot. Full visualization behind the ball, deep physiological breath, target lock, two waggle rhythm checks, committed swing.
2. **Quick-Trigger Cadence (Eliminating Freeze)**: 6 to 10 seconds. Designed for putting or under intense pressure when standing over the ball breeds doubt. One look, inhale-exhale, trigger movement.
3. **Wind / Back-Off / Restart Cadence**: Step-back protocol when disrupted. Definitively step away from the address position, take a 3-second reset breath, re-read the wind, step in with fresh commitment.

Important: Discovery, not doctrine. Do not invent arbitrary timing prescriptions (such as 'this must take exactly 27 seconds'). The platform provides flexible pacing support, while Coach Lornette Daye and experienced PGA Golf professionals define the authentic teaching model.

## Acceptance Criteria

- [ ] Technical review completed with Lornette Daye and certified PGA instructors
- [ ] Core 6-step routine remains the canonical foundation
- [ ] Visual pacing concepts documented without rigid artificial second limits
- [ ] Interactive cadence timing tool evaluated for mobile responsiveness
- [ ] Athlete field testing confirms no mechanical distraction during play

## Non-Goals

- Inventing arbitrary or doctrinaire timing prescriptions (e.g. rigid second counts)
- In-app metronome audio clicks during play (prohibited by Rules of Golf)
- Over-complicating junior golfers with rigid stopwatch micro-management

## Evidence Needed

- Observational pacing data from high school and collegiate competition rounds
- Approval from Coach Lornette on cadence reset phrasing

## V1.1 Decision Gate Evaluation

- [x] **Problem Evidence**: Simulated coach feedback noted rigid timing dogmas cause panic when disrupted by wind or lies.
- [x] **User Affected**: Competitive tournament players facing unpredictable weather, slow play, or putting freeze.
- [x] **Why Current V1 Is Insufficient**: Foundation 3 routine teaches steady structure, but lacks explicit guidance on when and how to back off gracefully.
- [x] **Smallest Useful Implementation**: Conceptual framework defining 3 situational cadences and a step-back reset protocol within Foundation 3.
- [x] **Privacy Implications**: Zero privacy risk; routine practice notes remain private to athlete.
- [x] **Mobile Implications**: Optional visual pulse guide in Quick Tools; zero illegal audio metronome signals.
- [x] **Acceptance Criteria**: 5 testable criteria defined; core 6-step routine preserved.
- [x] **Explicit Non-Goals**: No arbitrary second prescriptions, no in-round audio beeps, no stopwatch micro-management.

**Recommended Status**: `NEEDS_HUMAN_DECISION`  
*Rationale*: Pacing concepts and step-back mechanics are fully articulated. The 5 SME questions must be reviewed and answered by Coach Lornette Daye and certified PGA staff before production release.

## Decision Notes

- **2026-09-17**: Concept identified during coach simulation review.
- **2026-09-17**: Set status to `READY_FOR_DISCOVERY`. Exploratory research only; no code changes until approved.
- **2026-09-17**: Discovery sprint complete. Rebuttal of rigid clock doctrines, definition of 3 situational cadences, step-back mental mechanics, and 5 SME consultation questions documented in [`docs/superpowers/specs/2026-09-17-golf-v1-1-discovery-design.md`](../../docs/superpowers/specs/2026-09-17-golf-v1-1-discovery-design.md). Decision Gate evaluated; recommended status is `NEEDS_HUMAN_DECISION` (SME consultation). Zero production code written.
