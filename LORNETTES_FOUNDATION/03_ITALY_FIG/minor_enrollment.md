# Italian Minor Legal Consent Framework

**Workstream:** 03_ITALY_FIG  
**Release:** Italy FIG  
**Priority:** Research  
**Status:** RESEARCH_ONLY  
**Depends On:** GDPR_legal_review  
**Blocks:** NONE  
**Source:** Simulated institutional stress test  

## Problem

Italian legal standards (Codice Civile and D.Lgs. 101/2018 adapting GDPR Article 8) set the age of digital consent at 14 years old for information society services. For competitive athletes under 14, parental authorization is statutory. However, complex verification schemes (such as Italian government SPID or dual-parent digital signatures) could create immense friction for clubs and families if mandated prematurely.

## Why It Matters

Enrollment of Italian junior golfers (ages 12 to 18) must adhere to local parental consent laws. Over-engineering with national digital identity systems (SPID/CIE) when simple parental email verification is legally sufficient would stifle adoption. Conversely, failing to capture valid parental consent creates regulatory exposure.

## Proposed Direction

Investigate the legal and operational landscape before coding:
1. Verify whether Italian junior golf participation falls under informational society services (Article 8 GDPR, age 14 threshold) or sports federation licensing (where clubs collect parental consent upon membership).
2. Determine whether a dual-consent gateway (guardian email verification + athlete profile link) is legally adequate under Italian law.
3. Track SPID (Sistema Pubblico di Identità Digitale) and CIE (Carta di Identità Elettronica) requirements as potential institutional options, but do not hard-code them into the primary registration flow.
4. Evaluate a club-mediated consent model where the federation club certifies that parental consent is on file prior to issuing cohort redemption codes.

## Acceptance Criteria

- [ ] Legal determination of Italian age threshold (14 vs. 18) for athletic coaching platforms
- [ ] Club-mediated vs. direct-to-consumer parental consent workflow defined
- [ ] Specification for guardian email confirmation link if direct consent is required
- [ ] Explicit decision on SPID/CIE necessity based on formal institutional procurement advice

## Non-Goals

- Prematurely integrating SPID or CIE identity providers
- Building complex dual-parent notary verification without statutory requirement

## Evidence Needed

- Confirmation of club membership consent practices from FIG legal representatives
- Legal counsel approval of the proposed registration consent workflow

## Decision Notes

- **2026-09-17**: Logged in `RESEARCH_ONLY`. No engineering changes permitted until age rules are legally confirmed.
