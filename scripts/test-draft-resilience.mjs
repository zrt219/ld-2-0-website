// Automated test suite for Task 1: Reflection draft resilience
import assert from "node:assert";

// Mock localStorage for Node test environment
const storage = new Map();
global.localStorage = {
  getItem: (k) => (storage.has(k) ? storage.get(k) : null),
  setItem: (k, v) => storage.set(k, String(v)),
  removeItem: (k) => storage.delete(k),
  clear: () => storage.clear(),
  get length() {
    return storage.size;
  },
  key: (i) => Array.from(storage.keys())[i] || null,
};
global.window = {
  localStorage: global.localStorage,
  dispatchEvent: () => true,
};
Object.defineProperty(globalThis, "navigator", {
  value: { onLine: true },
  configurable: true,
  writable: true,
});

// Import functions from offline-store
const {
  makeDraftKey,
  saveOfflineDraft,
  getOfflineDraft,
  clearOfflineDraft,
  purgeAthleteDrafts,
} = await import("../src/lib/foundations/offline-store.js").catch(async () => {
  // If .js import fails in Node due to TS, import dynamically or test directly
  return import("../src/lib/foundations/offline-store.ts");
});

async function runTests() {
  console.log("--- RUNNING TASK 1 REFLECTION DRAFT RESILIENCE TESTS ---");

  // Test 1: Key format
  const key1 = makeDraftKey("user_123", 3, "cohort_fall2026");
  assert.strictEqual(
    key1,
    "foundation-draft:user_123:cohort_fall2026:3",
    "Key must be formatted with foundation-draft:userId:cohortId:lessonId"
  );
  console.log("✓ Test 1: Compound key structure correct");

  // Test 2: Save and retrieve draft
  await saveOfflineDraft(
    "user_123",
    3,
    "Discipline Systems",
    "Noticed fast backswing tempo",
    "Physiological breath worked",
    "Hold finish position",
    "cohort_fall2026"
  );

  const draft = await getOfflineDraft("user_123", 3, "cohort_fall2026");
  assert.ok(draft, "Draft should be retrieved");
  assert.strictEqual(draft.noticed, "Noticed fast backswing tempo");
  assert.strictEqual(draft.worked, "Physiological breath worked");
  assert.strictEqual(draft.repeated, "Hold finish position");
  console.log("✓ Test 2: Draft successfully persisted and retrieved");

  // Test 3: User isolation (User B cannot see User A's draft)
  const userBDraft = await getOfflineDraft("user_999", 3, "cohort_fall2026");
  assert.strictEqual(userBDraft, null, "User B must not see User A's draft");
  console.log("✓ Test 3: User isolation verified - zero draft crossover");

  // Test 4: Empty fields trigger draft deletion
  await saveOfflineDraft("user_123", 3, "Discipline Systems", "", "   ", "", "cohort_fall2026");
  const clearedDraft = await getOfflineDraft("user_123", 3, "cohort_fall2026");
  assert.strictEqual(clearedDraft, null, "Empty inputs must clear draft");
  console.log("✓ Test 4: Empty fields automatically clean up draft storage");

  // Test 5: Re-save and clear
  await saveOfflineDraft(
    "user_123",
    4,
    "Resilience After Setback",
    "Felt frustration on 14th hole",
    "5-second physical reset",
    "Release club into left hand",
    "cohort_fall2026"
  );
  let d4 = await getOfflineDraft("user_123", 4, "cohort_fall2026");
  assert.ok(d4, "Draft for lesson 4 exists");
  await clearOfflineDraft("user_123", 4, "cohort_fall2026");
  d4 = await getOfflineDraft("user_123", 4, "cohort_fall2026");
  assert.strictEqual(d4, null, "Draft 4 cleared after explicit clear");
  console.log("✓ Test 5: Explicit clear (simulating successful server save) removes local draft");

  // Test 6: Purge athlete drafts on account switch/logout
  await saveOfflineDraft("user_to_purge", 1, "Identity", "A", "B", "C");
  await saveOfflineDraft("user_to_purge", 2, "Mindset", "D", "E", "F");
  await saveOfflineDraft("user_keep", 1, "Identity", "Keep", "Keep", "Keep");

  await purgeAthleteDrafts("user_to_purge");
  const purged1 = await getOfflineDraft("user_to_purge", 1);
  const purged2 = await getOfflineDraft("user_to_purge", 2);
  const kept = await getOfflineDraft("user_keep", 1);

  assert.strictEqual(purged1, null, "Purged user draft 1 deleted");
  assert.strictEqual(purged2, null, "Purged user draft 2 deleted");
  assert.ok(kept, "Other user's draft preserved");
  console.log("✓ Test 6: Purge on logout deletes only target athlete drafts");

  console.log("ALL TASK 1 TESTS PASSED!\n");
}

runTests().catch((err) => {
  console.error("Test failed:", err);
  process.exit(1);
});
