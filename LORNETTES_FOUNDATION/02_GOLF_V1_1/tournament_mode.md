# Tournament Mode

**Workstream:** 02_GOLF_V1_1  
**Release:** Golf V1.1  
**Priority:** V1.1 (Priority 1)  
**Status:** DISCOVERY_COMPLETE  
**Depends On:** 01_MVP_CLUB  
**Blocks:** NONE  
**Source:** Simulated institutional stress test  

## Problem

During active tournament weeks (e.g. state amateurs, junior invitationals, college qualifiers), competitive golfers cannot engage with lengthy 15-minute video lessons or deep theoretical writing on Thursday through Sunday. When forced into normal LMS coursework during match play or medal play rounds, athletes either skip modules or experience mental cognitive overload right before teeing off.

## Why It Matters

Golfers participate in this program specifically to play their best when it matters most. If the platform demands passive video consumption during high-stakes competition days, it contradicts Lornette's teaching on focus and energy management.

## Proposed Direction

Introduce an adaptive competition-week presentation layer:
The canonical 10-week program remains completely unchanged. Tournament Mode adjusts how the active week's content is delivered across the weekly rhythm:
- **Monday / Tuesday (Deep Foundation Work)**: Normal video lesson, workbook reflection, inner dialogue, and core Foundation tools.
- **Wednesday (Course Preparation & Strategy)**: Tactical focus, pin sheet visualization, wind and weather plan, decision-making boundaries.
- **Thursday through Sunday (Execution Mode)**: Clean, high-leverage on-course interface surfacing only critical execution tools:
  - 5-Second Physical Reset
  - Pre-Shot Routine trigger
  - Pressure Plan & physiological sigh
  - Focus anchor cue
  - Daily competition intention

Tournament Mode is strictly a presentation and delivery filter. It is not a separate curriculum or an alternative 10-week program.

## Acceptance Criteria

- [ ] 10-Week / 10-Foundation architecture remains completely unchanged
- [ ] Athlete can toggle Tournament Mode for specific calendar weeks
- [ ] Monday and Tuesday present full Foundation video and reflection tasks
- [ ] Wednesday transitions to tactical pre-round preparation
- [ ] Thursday through Sunday presents stripped-down execution tools
- [ ] Zero duplicate courseware or secondary curriculum databases created
- [ ] Fast, 1-tap mobile access preserved on competition days
- [ ] Athlete can return to Standard Mode at any time without data loss

## Non-Goals

- Creating a separate or alternative 10-week tournament curriculum
- Live score tracking, yardage book digitizing, or stroke statistics
- Mandatory participation (athletes can remain in Standard Mode year-round)

## Evidence Needed

- Evidence from at least one of: real athlete pilot data, club staff feedback, tournament schedule conflict logs, or explicit Lornette product approval
- Usability feedback from competitive juniors playing in 36-hole weekend events

## V1.1 Decision Gate Evaluation

- [x] **Problem Evidence**: Simulated institutional stress test identified tournament week cognitive overload; requires real pilot verification.
- [x] **User Affected**: Competitive junior tour athletes (ages 14-18) and amateur tournament players.
- [x] **Why Current V1 Is Insufficient**: Standard LMS layout pushes 15-minute video and long essay reflections during active 36-hole weekend events.
- [x] **Smallest Useful Implementation**: Option D hybrid toggle delivering stripped 1-tap mobile execution launcher for existing Quick Tools.
- [x] **Privacy Implications**: Zero privacy risk; competition intention and debrief reflections remain sanctuary-grade private to participant and Lornette.
- [x] **Mobile Implications**: High-contrast outdoor theme (12.8:1), 52px touch targets, lower thumb-zone placement, sub-50ms offline cache.
- [x] **Acceptance Criteria**: 8 testable criteria defined; 10-week canonical lock preserved.
- [x] **Explicit Non-Goals**: No GPS, no live scoring, no swing video analysis, no audio metronome.

**Recommended Status**: `NEEDS_REAL_PILOT_EVIDENCE`  
*Rationale*: Discovery and architecture are 100% complete, but production coding should await behavioral validation from the Mountain Ridge pilot.

## Decision Notes

- **2026-09-17**: Initial concept proposed during Mountain Ridge debrief simulation.
- **2026-09-17**: Locked as V1.1 Priority 1. Marked `READY_FOR_DISCOVERY`. Production implementation blocked until real pilot evidence is collected.
- **2026-09-17**: Discovery sprint complete. Full architectural design, Option D hybrid toggle model, lifecycle state model, outdoor mobile UX contracts, and domain TypeScript definitions documented in [`docs/superpowers/specs/2026-09-17-golf-v1-1-discovery-design.md`](../../docs/superpowers/specs/2026-09-17-golf-v1-1-discovery-design.md). Decision Gate evaluated; recommended status is `NEEDS_REAL_PILOT_EVIDENCE`. Zero production code written.
