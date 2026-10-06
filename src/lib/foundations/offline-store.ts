import { ProgramTrack } from "./store";

export type OfflineReflectionRecord = {
  id: string; // athleteId_track_lessonId or legacy
  athleteId: string;
  lessonId: number;
  track?: ProgramTrack;
  foundationTitle: string;
  noticed: string;
  worked: string;
  repeated: string;
  status: "draft" | "pending_sync" | "synced";
  updatedAt: string;
};

export type SyncStatusDetail = {
  isOnline: boolean;
  pendingCount: number;
  isSyncing: boolean;
  lastSyncedAt: string | null;
};

const DB_NAME = "ld_foundations_offline_db";
const DB_VERSION = 1;
const STORE_REFLECTIONS = "reflections";
const STORE_OUTBOX = "sync_outbox";
export const SYNC_STATUS_EVENT = "ld_offline_sync_status";

function openDB(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    if (typeof window === "undefined" || !window.indexedDB) {
      reject(new Error("IndexedDB not supported"));
      return;
    }
    const request = indexedDB.open(DB_NAME, DB_VERSION);
    request.onupgradeneeded = () => {
      const db = request.result;
      if (!db.objectStoreNames.contains(STORE_REFLECTIONS)) {
        db.createObjectStore(STORE_REFLECTIONS, { keyPath: "id" });
      }
      if (!db.objectStoreNames.contains(STORE_OUTBOX)) {
        db.createObjectStore(STORE_OUTBOX, { keyPath: "id" });
      }
    };
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

export function makeDraftKey(
  athleteId: string,
  lessonId: number,
  cohortId?: string | null,
  track?: ProgramTrack | null
): string {
  const safeCohort = cohortId && cohortId.trim() ? cohortId.trim() : "default";
  const safeTrack = track || "golf";
  return `foundation-draft:${athleteId}:${safeCohort}:${safeTrack}:${lessonId}`;
}

export function notifySyncStatus(detail: Partial<SyncStatusDetail>) {
  if (typeof window === "undefined") return;
  const isOnline = typeof navigator !== "undefined" ? navigator.onLine : true;
  const event = new CustomEvent<SyncStatusDetail>(SYNC_STATUS_EVENT, {
    detail: {
      isOnline,
      pendingCount: detail.pendingCount ?? 0,
      isSyncing: detail.isSyncing ?? false,
      lastSyncedAt: detail.lastSyncedAt ?? null,
    },
  });
  window.dispatchEvent(event);
}

export async function saveOfflineDraft(
  athleteId: string,
  lessonId: number,
  foundationTitle: string,
  noticed: string,
  worked: string,
  repeated: string,
  cohortId?: string | null,
  track?: ProgramTrack | null
): Promise<void> {
  const id = makeDraftKey(athleteId, lessonId, cohortId, track);
  const isAllEmpty = !noticed.trim() && !worked.trim() && !repeated.trim();
  if (isAllEmpty) {
    await clearOfflineDraft(athleteId, lessonId, cohortId, track);
    return;
  }

  const record: OfflineReflectionRecord = {
    id,
    athleteId,
    lessonId,
    track: track || "golf",
    foundationTitle,
    noticed,
    worked,
    repeated,
    status: "draft",
    updatedAt: new Date().toISOString(),
  };

  try {
    const db = await openDB();
    await new Promise<void>((resolve, reject) => {
      const tx = db.transaction([STORE_REFLECTIONS], "readwrite");
      const store = tx.objectStore(STORE_REFLECTIONS);
      store.put(record);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error);
    });
  } catch {
    if (typeof window !== "undefined") {
      try {
        localStorage.setItem(id, JSON.stringify(record));
      } catch {}
    }
  }
}

export async function getOfflineDraft(
  athleteId: string,
  lessonId: number,
  cohortId?: string | null,
  track?: ProgramTrack | null
): Promise<OfflineReflectionRecord | null> {
  const primaryId = makeDraftKey(athleteId, lessonId, cohortId, track);
  const fallbackLegacyCohortId = `foundation-draft:${athleteId}:${cohortId || "default"}:${lessonId}`;
  const fallbackLegacyId = `${athleteId}_${lessonId}`;

  try {
    const db = await openDB();
    const record = await new Promise<OfflineReflectionRecord | null>((resolve) => {
      const tx = db.transaction([STORE_REFLECTIONS], "readonly");
      const store = tx.objectStore(STORE_REFLECTIONS);
      const req = store.get(primaryId);
      req.onsuccess = () => {
        if (req.result) {
          resolve(req.result);
        } else {
          // Check fallback legacy trackless key
          const fallbackReq1 = store.get(fallbackLegacyCohortId);
          fallbackReq1.onsuccess = () => {
            if (fallbackReq1.result) {
              resolve(fallbackReq1.result);
            } else {
              // Check fallback legacy id
              const fallbackReq2 = store.get(fallbackLegacyId);
              fallbackReq2.onsuccess = () => resolve(fallbackReq2.result || null);
              fallbackReq2.onerror = () => resolve(null);
            }
          };
          fallbackReq1.onerror = () => resolve(null);
        }
      };
      req.onerror = () => resolve(null);
    });

    if (record) return record;
  } catch {}

  // Fallback to localStorage
  if (typeof window !== "undefined") {
    try {
      const raw =
        localStorage.getItem(primaryId) ||
        localStorage.getItem(fallbackLegacyCohortId) ||
        localStorage.getItem(fallbackLegacyId) ||
        localStorage.getItem(`ld_reflection_draft_${athleteId}_lesson_${lessonId}`);
      if (raw) {
        const parsed = JSON.parse(raw);
        return {
          id: primaryId,
          athleteId,
          lessonId,
          track: parsed.track || track || "golf",
          foundationTitle: parsed.foundationTitle || "",
          noticed: parsed.noticed || "",
          worked: parsed.worked || "",
          repeated: parsed.repeated || "",
          status: "draft",
          updatedAt: parsed.updatedAt || new Date().toISOString(),
        };
      }
    } catch {}
  }
  return null;
}

export async function clearOfflineDraft(
  athleteId: string,
  lessonId: number,
  cohortId?: string | null,
  track?: ProgramTrack | null
): Promise<void> {
  const primaryId = makeDraftKey(athleteId, lessonId, cohortId, track);
  const fallbackLegacyCohortId = `foundation-draft:${athleteId}:${cohortId || "default"}:${lessonId}`;
  const legacyId = `${athleteId}_${lessonId}`;

  try {
    const db = await openDB();
    await new Promise<void>((resolve, reject) => {
      const tx = db.transaction([STORE_REFLECTIONS], "readwrite");
      const store = tx.objectStore(STORE_REFLECTIONS);
      store.delete(primaryId);
      store.delete(fallbackLegacyCohortId);
      store.delete(legacyId);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error);
    });
  } catch {}

  if (typeof window !== "undefined") {
    try {
      localStorage.removeItem(primaryId);
      localStorage.removeItem(fallbackLegacyCohortId);
      localStorage.removeItem(legacyId);
      localStorage.removeItem(`ld_reflection_draft_${athleteId}_lesson_${lessonId}`);
    } catch {}
  }
}

export async function purgeAthleteDrafts(athleteId: string): Promise<void> {
  try {
    const db = await openDB();
    await new Promise<void>((resolve, reject) => {
      const tx = db.transaction([STORE_REFLECTIONS], "readwrite");
      const store = tx.objectStore(STORE_REFLECTIONS);
      const req = store.getAll();
      req.onsuccess = () => {
        const records: OfflineReflectionRecord[] = req.result || [];
        records.forEach((r) => {
          if (r.athleteId === athleteId) {
            store.delete(r.id);
          }
        });
      };
      req.onerror = () => reject(req.error);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error);
    });
  } catch {}

  if (typeof window !== "undefined") {
    try {
      const prefix = `foundation-draft:${athleteId}:`;
      const keysToRemove: string[] = [];
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && (key.startsWith(prefix) || key.startsWith(`ld_reflection_draft_${athleteId}_`))) {
          keysToRemove.push(key);
        }
      }
      keysToRemove.forEach((k) => localStorage.removeItem(k));
    } catch {}
  }
}

/**
 * GDPR Data Erasure helper: removes all local drafts, reflections, and outbox records
 * for a specific athlete from IndexedDB and localStorage (Right to be Forgotten).
 */
export async function purgeAthleteAllData(athleteId: string): Promise<void> {
  try {
    const db = await openDB();
    await new Promise<void>((resolve, reject) => {
      const tx = db.transaction([STORE_REFLECTIONS, STORE_OUTBOX], "readwrite");
      const refStore = tx.objectStore(STORE_REFLECTIONS);
      const outboxStore = tx.objectStore(STORE_OUTBOX);

      const refReq = refStore.getAll();
      refReq.onsuccess = () => {
        const records: OfflineReflectionRecord[] = refReq.result || [];
        records.forEach((r) => {
          if (r.athleteId === athleteId) {
            refStore.delete(r.id);
          }
        });
      };
      refReq.onerror = () => reject(refReq.error);

      const outboxReq = outboxStore.getAll();
      outboxReq.onsuccess = () => {
        const records: OfflineReflectionRecord[] = outboxReq.result || [];
        records.forEach((r) => {
          if (r.athleteId === athleteId) {
            outboxStore.delete(r.id);
          }
        });
      };
      outboxReq.onerror = () => reject(outboxReq.error);

      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error);
    });
  } catch {}

  if (typeof window !== "undefined") {
    try {
      const prefix = `foundation-draft:${athleteId}:`;
      const outboxPrefix = `ld_outbox_${athleteId}_`;
      const keysToRemove: string[] = [];
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (
          key &&
          (key.startsWith(prefix) ||
            key.startsWith(`ld_reflection_draft_${athleteId}_`) ||
            key.startsWith(outboxPrefix) ||
            key.includes(athleteId))
        ) {
          keysToRemove.push(key);
        }
      }
      keysToRemove.forEach((k) => localStorage.removeItem(k));
    } catch {}
  }

  const outbox = await getPendingOutboxSyncs();
  notifySyncStatus({ pendingCount: outbox.length });
}

export async function queueReflectionSync(
  athleteId: string,
  lessonId: number,
  foundationTitle: string,
  noticed: string,
  worked: string,
  repeated: string,
  track?: ProgramTrack | null
): Promise<void> {
  const safeTrack = track || "golf";
  const id = `${athleteId}_${safeTrack}_${lessonId}`;
  const record: OfflineReflectionRecord = {
    id,
    athleteId,
    lessonId,
    track: safeTrack,
    foundationTitle,
    noticed,
    worked,
    repeated,
    status: "pending_sync",
    updatedAt: new Date().toISOString(),
  };

  try {
    const db = await openDB();
    await new Promise<void>((resolve, reject) => {
      const tx = db.transaction([STORE_REFLECTIONS, STORE_OUTBOX], "readwrite");
      tx.objectStore(STORE_REFLECTIONS).put(record);
      tx.objectStore(STORE_OUTBOX).put(record);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error);
    });
  } catch {
    if (typeof window !== "undefined") {
      try {
        localStorage.setItem(`ld_outbox_${id}`, JSON.stringify(record));
      } catch {}
    }
  }

  const outbox = await getPendingOutboxSyncs();
  notifySyncStatus({ pendingCount: outbox.length });
}

export async function clearSyncedOutboxRecord(id: string): Promise<void> {
  try {
    const db = await openDB();
    await new Promise<void>((resolve, reject) => {
      const tx = db.transaction([STORE_OUTBOX], "readwrite");
      tx.objectStore(STORE_OUTBOX).delete(id);
      tx.oncomplete = () => resolve();
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error);
    });
  } catch {
    if (typeof window !== "undefined") {
      try {
        localStorage.removeItem(`ld_outbox_${id}`);
      } catch {}
    }
  }

  const outbox = await getPendingOutboxSyncs();
  notifySyncStatus({ pendingCount: outbox.length });
}

export async function getPendingOutboxSyncs(): Promise<OfflineReflectionRecord[]> {
  try {
    const db = await openDB();
    return new Promise((resolve) => {
      const tx = db.transaction([STORE_OUTBOX], "readonly");
      const store = tx.objectStore(STORE_OUTBOX);
      const req = store.getAll();
      req.onsuccess = () => resolve(req.result || []);
      req.onerror = () => resolve([]);
    });
  } catch {
    const outbox: OfflineReflectionRecord[] = [];
    if (typeof window !== "undefined") {
      try {
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i);
          if (key && key.startsWith("ld_outbox_")) {
            const raw = localStorage.getItem(key);
            if (raw) outbox.push(JSON.parse(raw));
          }
        }
      } catch {}
    }
    return outbox;
  }
}

export async function flushOutboxSync(
  syncItemHandler?: (item: OfflineReflectionRecord) => Promise<boolean>
): Promise<{ synced: number; remaining: number }> {
  if (typeof navigator !== "undefined" && !navigator.onLine) {
    const outbox = await getPendingOutboxSyncs();
    return { synced: 0, remaining: outbox.length };
  }

  const pending = await getPendingOutboxSyncs();
  if (pending.length === 0) {
    return { synced: 0, remaining: 0 };
  }

  notifySyncStatus({ isSyncing: true, pendingCount: pending.length });
  let synced = 0;

  for (const item of pending) {
    let success = false;
    if (syncItemHandler) {
      try {
        success = await syncItemHandler(item);
      } catch {
        success = false;
      }
    } else {
      // Default: attempt Supabase sync via dynamic import
      try {
        const { createClient } = await import("@/lib/supabase/client");
        const supabase = createClient();
        const { data: { user } } = await supabase.auth.getUser();
        if (user) {
          const { data: cohortMembers } = await supabase
            .from("cohort_members")
            .select("*")
            .eq("profile_id", user.id)
            .limit(1);
          const cohort_id = cohortMembers?.[0]?.cohort_id;
          if (cohort_id) {
            const { data: existing } = await supabase
              .from("weekly_reflections")
              .select("id")
              .eq("profile_id", user.id)
              .eq("week_number", item.lessonId)
              .single();

            if (existing) {
              await supabase
                .from("weekly_reflections")
                .update({
                  what_noticed: item.noticed,
                  what_worked: item.worked,
                  what_repeat: item.repeated,
                  submitted_at: item.updatedAt,
                })
                .eq("id", existing.id);
            } else {
              await supabase.from("weekly_reflections").insert({
                cohort_id,
                week_number: item.lessonId,
                profile_id: user.id,
                prompt_question: item.foundationTitle,
                response_text: "Reflection",
                what_noticed: item.noticed,
                what_worked: item.worked,
                what_repeat: item.repeated,
              });
            }
            success = true;
          }
        }
      } catch {
        success = false;
      }
    }

    if (success) {
      await clearSyncedOutboxRecord(item.id);
      synced++;
    }
  }

  const remainingRecords = await getPendingOutboxSyncs();
  notifySyncStatus({
    isSyncing: false,
    pendingCount: remainingRecords.length,
    lastSyncedAt: synced > 0 ? new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }) : null,
  });

  return { synced, remaining: remainingRecords.length };
}