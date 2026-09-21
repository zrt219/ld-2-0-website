# Workstream 02: Golf V1.1 (Active Future Backlog)

**Workstream:** 02_GOLF_V1_1  
**Status:** Active Future Backlog  
**Release Target:** Golf V1.1  

---

## Purpose

Improve the competitive Golf experience based on evidence from real club and athlete usage without destabilizing the validated Golf V1 core.

This directory is an active future backlog, not a dead idea archive. Discovery, scenario drafting, and technical feasibility research may begin immediately, but production implementation requires passing the Golf V1.1 Decision Gate.

---

## Core Principles

1. **Preserve 10 Athletic Foundations**: The canonical 10-week / 10-Foundation architecture is locked. Features add context, not more weeks or alternative curricula.
2. **Preserve Lornette-Led Human Delivery**: Technology serves Coach Lornette's guidance and personal touch, never replacing human connection.
3. **Performance Edge Remains Methodology**: The framework (Focus, Pre-Shot Routine, Pressure, Visualization, Reset, Decision-Making, Preparation, Confidence) is the tooling layer.
4. **Add Context, Not Unnecessary Curriculum**: Solve real competition friction rather than piling on LMS coursework.
5. **Real Pilot Evidence Outranks Simulated Feedback**: Priorities adapt to verified operational data from paying clubs and active golfers.
6. **Do Not Expand Into Another Sport**: Maintain absolute focus on Golf excellence before multi-sport generalization.
7. **Every Feature Must Solve Observed Golfer or Club Friction**: Never build speculative features without concrete player demand.

---

## V1.1 Kanban Lifecycle States

- `BACKLOG`: Captured concept awaiting prioritization or preliminary evidence.
- `READY_FOR_DISCOVERY`: Problem identified; exploring user needs and functional scope.
- `CONTENT_DESIGN`: Drafting prompts, scenarios, scripts, or instructional copy.
- `TECHNICAL_DESIGN`: Architecture, data modeling, and performance evaluation.
- `READY`: All decision gate criteria met; ready for sprint scheduling.
- `IN_PROGRESS`: Actively under development in isolated branch.
- `VALIDATING`: Internal QA, security checks, and pilot review.
- `DONE`: Merged into production release and verified.
- `BLOCKED`: Work suspended pending dependency resolution or user feedback.

---

## Golf V1.1 Decision Gate

Before any item transitions from discovery into `READY` for production implementation, it must satisfy all 8 requirements:
1. **Problem Evidence**: Verified data or direct observation from real club pilots.
2. **User Affected**: Exact participant, coach, or parent persona clearly defined.
3. **Why Current V1 Is Insufficient**: Concrete limitation documented in current release.
4. **Smallest Useful Implementation**: Lean MVP scope defined without feature creep.
5. **Privacy Implications**: Verified zero risk to participant reflection confidentiality.
6. **Mobile Implications**: Bandwidth, battery, and outdoor usability verified.
7. **Acceptance Criteria**: Testable, unambiguous checkbox deliverables.
8. **Explicit Non-Goals**: Hard boundaries established against scope creep.

---

## Master Discovery Specification

The comprehensive product and architectural discovery specification for Golf V1.1 is documented at:
- [`docs/superpowers/specs/2026-09-17-golf-v1-1-discovery-design.md`](../../docs/superpowers/specs/2026-09-17-golf-v1-1-discovery-design.md)

This document covers all 44 discovery items across Tournament Mode, Match Play Scenarios, and Variable Cadence, including full scenario scripts, USGA/R&A rule references, state models, and domain TypeScript definitions. Zero production feature code was written.

---

## Initial Priority Order

| Priority | Item | Status | Focus Area |
|---|---|---|---|
| **V1.1 Priority 1** | [Tournament Mode](./tournament_mode.md) | `NEEDS_REAL_PILOT_EVIDENCE` | Competition-week rhythm adaptation |
| **V1.1 Priority 2** | [Match Play Scenarios](./match_play_scenarios.md) | `NEEDS_HUMAN_DECISION` | High-leverage competitive decision bank |
| **V1.1 Priority 3** | [Variable Cadence](./variable_cadence.md) | `NEEDS_HUMAN_DECISION` | Dynamic pre-shot routine pacing |
| **V1.1 Priority 4** | [Coach Reinforcement](./coach_reinforcement.md) | `BACKLOG` (Deferred) | Structured practice and tee-line cues |
| **V1.1 Priority 5** | [Parent Companion](./parent_companion.md) | `BACKLOG` (Deferred) | Junior development boundary guidance |

