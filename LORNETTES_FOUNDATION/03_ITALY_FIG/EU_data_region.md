# European Cloud Data Residency Migration

**Workstream:** 03_ITALY_FIG  
**Release:** Italy FIG  
**Priority:** Research  
**Status:** RESEARCH_ONLY  
**Depends On:** GDPR_legal_review, DPA  
**Blocks:** NONE  
**Source:** Simulated institutional stress test  

## Problem

Italian public bodies and sports federations often demand or strongly prefer European Union cloud data residency (e.g. Frankfurt, Milan, Dublin) to simplify compliance with Schrems II transfer rulings and avoid trans-Atlantic data transfer scrutiny. The current platform database lives in North America.

## Why It Matters

If FIG procurement mandates that athlete reflections, identities, and assessment data remain strictly within the European Economic Area (EEA), the platform must have a clear technical roadmap to instantiate an EU-hosted tenant without breaking global production operations.

## Proposed Direction

Conduct technical architecture feasibility research:
1. **Supabase EU Regional Availability**: Evaluate provisioning a dedicated European Supabase instance (e.g. `eu-central-1` Frankfurt or `eu-west-1` Ireland).
2. **Multi-Region Tenant Architecture**: Evaluate whether European federations should operate on an isolated regional database instance or whether a global multi-tenant database is sustainable under Standard Contractual Clauses.
3. **Storage & Auth Isolation**: Map storage buckets and authentication JWT issuers to EU endpoints for European cohorts.
4. **Backup & Disaster Recovery**: Ensure database snapshots, automated backups, and log aggregators remain within EU geographic borders.

Important: Do not migrate existing production infrastructure or incur secondary cloud costs merely because this backlog item exists. This is an architectural contingency plan.

## Acceptance Criteria

- [ ] Technical assessment document outlining Supabase EU deployment steps and costs
- [ ] Multi-region environment configuration documented in Next.js environment schema
- [ ] Latency and CDN routing analysis completed for European end-users
- [ ] Database migration and tenant-isolation procedures tested in staging environment

## Non-Goals

- Migrating current North American production database or staging infrastructure
- Provisioning redundant cloud environments prior to executed institutional contracts

## Evidence Needed

- Explicit procurement mandate from Italian federation requiring EU-only data residency
- Authorized commercial budget for multi-region cloud operations

## Decision Notes

- **2026-09-17**: Logged in `RESEARCH_ONLY`. Technical exploration only. No live cloud resources to be provisioned.
