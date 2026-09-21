# Lornette's Foundation Product Roadmap

Welcome to the canonical roadmap and backlog repository for Lornette's Foundation: Golf (Powered by the Performance Edge Framework).

This system maintains three separate, decoupled workstreams to ensure production stability, disciplined feature evolution, and strict legal/regulatory isolation.

---

## The Three Dedicated Workstreams

### 1. `01_MVP_CLUB/` (Current Club MVP Hardening)
- **Scope**: Critical operational issues that must be solved for the first reliable real-world club MVP.
- **Focus**: Reflection draft protection, database-driven cohort capacity, operational roster visibility without privacy bleed, mobile session reliability, fast offline field tools, PGA Coach Companion, and board-ready cohort reporting.
- **Status**: Production Hardening. This is the immediate release gate for live club delivery.

### 2. `02_GOLF_V1_1/` (Active Future Golf Backlog)
- **Scope**: Golf product enhancements that are valuable after the first-club MVP foundation is stable.
- **Focus**: Tournament Mode presentation layer, Match Play decision scenario bank, variable pre-shot routine cadence, junior parent weekly companion, and advanced coach reinforcement.
- **Status**: Active Future Backlog. Discovery and content design may proceed in parallel, but code cannot merge into production without passing the Golf V1.1 Decision Gate.

### 3. `03_ITALY_FIG/` (Institutional European & Italian Federation Expansion)
- **Scope**: Institutional European and Italian Golf Federation (Federazione Italiana Golf: FIG) requirements.
- **Focus**: Italian translation (`it-IT`), FIG minor safeguarding workflows, GDPR legal review, minor consent frameworks, institutional DPA, EU data residency migration, and federation-level rollup reporting.
- **Status**: Research Only. Strictly decoupled from Canadian and US private-club MVP development.

---

## Core Invariant Rule

> **DO NOT USE ITALY / FIG REQUIREMENTS TO BLOCK OR EXPAND THE FIRST CLUB MVP.**
>
> Requirements from `03_ITALY_FIG` belong strictly to a separate future institutional procurement track. They must never delay, block, or introduce unnecessary complexity into the current Club MVP or Golf V1.1 core.

---

## Backlog Item Template & Governance

Every backlog item across all three directories adheres to a standardized schema:
- Metadata Header (`Workstream`, `Release`, `Priority`, `Status`, `Depends On`, `Blocks`, `Source`)
- Problem Description
- Why It Matters
- Proposed Direction
- Concrete Acceptance Criteria (Checkboxes)
- Explicit Non-Goals
- Evidence Needed
- Chronological Decision Notes

### Source Labeling Standard
Any issue or requirement originating from hypothetical simulation, club roleplay, or synthetic federations must be explicitly labeled:
`Source: Simulated institutional stress test`
Only issues verified with real paying clubs, live athletes, or verified legal counsel receive live operational status.
