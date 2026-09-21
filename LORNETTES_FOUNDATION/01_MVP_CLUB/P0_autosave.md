# Reflection Draft Loss Protection

**Workstream:** 01_MVP_CLUB  
**Release:** Club MVP  
**Priority:** P0  
**Status:** DONE  
**Depends On:** NONE  
**Blocks:** 02_GOLF_V1_1  
**Source:** Simulated institutional stress test  

## Problem

A golfer typing a reflection on mobile may switch apps, experience signal loss on the course, reload the page, or have the mobile browser suspend the tab before the server save completes. Without client-side draft resilience, unsaved reflection text is lost, frustrating athletes and degrading program engagement.

## Why It Matters

Athletes invest genuine emotional energy into reflecting on mistakes, pressure triggers, and composure routines. Losing a paragraph of deep personal reflection breaks trust with the platform and leads to shallow or abandoned entries.

## Proposed Direction

Implement a resilient, client-side draft layer using compound keying:
`foundation-draft:${userId}:${cohortOrEnrollmentId}:${lessonId}`
Debounce local persistence (500 to 1000ms) to IndexedDB with automatic localStorage fallback. Compare timestamps between local drafts and server records so newer drafts are never overwritten by stale server data. Delete the local draft only after verified server persistence.

## Acceptance Criteria

- [x] Unsaved draft survives page reload
- [x] Unsaved draft survives transient network failure
- [x] Draft does not leak across participants (isolated by user ID)
- [x] Successful Supabase save clears local draft
- [x] Reflection text never enters analytics or console logs
- [x] Logout or account-switch cannot expose prior participant draft
- [x] Timestamp comparison (`draftTime > serverTime`) prevents stale server overwrite
- [x] Outbox queue automatically retries syncing when connection restores

## Non-Goals

- Replacing Supabase as canonical, authoritative storage
- Building a full offline-first database sync engine for the entire site
- Sending unsaved drafts to server logs or telemetry

## Evidence Needed

- Client draft unit test verifying compound keying, user isolation, and cleanup on save
- Browser interruption simulation (network cut, reload, background tab)
- Production build verification

## Decision Notes

- **2026-09-17**: Initial simulated stress test identified draft loss on Safari tab sleep.
- **2026-09-17**: Built `src/lib/foundations/offline-store.ts` with dual IndexedDB stores (`reflections`, `sync_outbox`) and localStorage fallback.
- **2026-09-17**: Connected to `src/app/foundations/lessons/page.tsx` with 750ms debounce and timestamp protection. Verified 6/6 tests passing in `scripts/test-draft-resilience.mjs`.
