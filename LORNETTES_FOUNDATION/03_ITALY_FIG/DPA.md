# Institutional Data Processing Agreement

**Workstream:** 03_ITALY_FIG  
**Release:** Italy FIG  
**Priority:** Research  
**Status:** RESEARCH_ONLY  
**Depends On:** GDPR_legal_review  
**Blocks:** NONE  
**Source:** Simulated institutional stress test  

## Problem

Institutional procurement with the Federazione Italiana Golf or major Italian regional academies requires an executed Data Processing Agreement (DPA) adhering to Article 28 of GDPR. The DPA must clearly define processing instructions, security measures, subprocessor disclosures, and breach notification SLAs.

## Why It Matters

Public and semi-public sports federations in Italy are subject to public procurement rules and administrative auditing. Delivering programs without an enterprise-grade DPA will halt institutional contract execution during legal review.

## Proposed Direction

Draft a standardized institutional Data Processing Agreement in coordination with European privacy counsel:
1. Clearly document platform subprocessors (e.g. Supabase, Vercel, AWS, Stripe).
2. Detail technical and organizational security measures (TOMs): AES-256 encryption at rest, TLS 1.3 in transit, PostgreSQL row-level security, role-based access control, least-privilege principles.
3. Establish 72-hour personal data breach notification workflows aligned with GDPR Article 33.
4. Define post-termination data return and deletion timelines (e.g. 30 days post-contract).
5. Incorporate European Commission Standard Contractual Clauses (Module Two: Controller-to-Processor or Module Three: Processor-to-Processor) where cross-border transfers occur.

## Acceptance Criteria

- [ ] Standardized Article 28 GDPR DPA template finalized and vetted by European counsel
- [ ] Subprocessor schedule published with hosting locations and function descriptions
- [ ] Security Schedule (TOMs) documented with verified infrastructure practices
- [ ] Incident response and 72-hour breach notification procedure established

## Non-Goals

- Negotiating bespoke, non-standard DPAs prior to institutional procurement interest
- Modifying production database architecture before contractual terms are agreed

## Evidence Needed

- Standard DPA requirements checklist from FIG legal procurement division
- Final review from external privacy counsel

## Decision Notes

- **2026-09-17**: Logged in `RESEARCH_ONLY`. Legal drafting prioritized only upon active institutional commercial engagement.
