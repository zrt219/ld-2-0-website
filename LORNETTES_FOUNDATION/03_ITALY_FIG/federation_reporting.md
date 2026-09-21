# Multi-Club Federation Rollup Reporting

**Workstream:** 03_ITALY_FIG  
**Release:** Italy FIG  
**Priority:** Research  
**Status:** RESEARCH_ONLY  
**Depends On:** GDPR_legal_review, DPA  
**Blocks:** NONE  
**Source:** Simulated institutional stress test  

## Problem

Federation leadership (e.g. FIG National Technical Directors or Regional Committees) oversee dozens of member clubs and regional training centers. At this tier, leadership requires macro-level aggregate reporting across multiple clubs to track youth participation, milestone completion, and retention without violating athlete privacy.

## Why It Matters

National federations invest in youth development at scale. Demonstrating aggregate outcome trends across regional hubs justifies continued public sports grant funding and national training sponsorship.

## Proposed Direction

Explore an institutional federation reporting dashboard architecture:
1. **Multi-Club Aggregation**: Roll up enrollment, milestone progress, and completion percentages across participating federation clubs.
2. **Regional Center Comparisons**: Anonymized macro benchmarks across geographic regions (e.g. Lombardy, Tuscany, Lazio) without exposing club-level embarrassment or individual athlete data.
3. **Safeguarding-Aware Role Permissions**: Federation officers have macro analytics access only. They have zero visibility into participant names, contact info, or written reflections.
4. **Institutional Export Formats**: Standardized annual sports report exports formatted for Italian National Olympic Committee (CONI) and federation board reviews.

Core Invariant: Multi-club rollups must never weaken individual athlete privacy. Raw reflections and private assessment entries remain completely inaccessible to federation officials.

## Acceptance Criteria

- [ ] Technical architecture specification for multi-club rollup queries
- [ ] Role-based access control definition for federation-tier administrators
- [ ] Anonymization and k-anonymity threshold rules (minimum 10 participants per reporting group)
- [ ] Export format specifications aligned with CONI sports reporting standards

## Non-Goals

- Granting national federation officials surveillance access to individual athlete accounts
- Ranking or public shaming of individual junior golfers based on mental milestone progress

## Evidence Needed

- Direct requirements interview with FIG technical committee leadership
- Validated institutional demand for national aggregate dashboards

## Decision Notes

- **2026-09-17**: Logged in `RESEARCH_ONLY`. Architectural concept documented for future European institutional expansion.
