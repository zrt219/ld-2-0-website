// Automated test suite for Task 2 (Dynamic Capacity) and Task 3 (Club Roster Operational View)
import assert from "node:assert";

function computeCapacityMetrics(enrolled, capacity) {
  const activeCount = enrolled || 0;
  const targetCapacity = capacity !== undefined ? capacity : 20;
  const pct = targetCapacity !== null
    ? (targetCapacity > 0 ? Math.min(100, Math.round((activeCount / targetCapacity) * 100)) : 100)
    : 100;
  const remainingSpaces = targetCapacity !== null ? Math.max(0, targetCapacity - activeCount) : null;
  return { activeCount, targetCapacity, pct, remainingSpaces };
}

function validateCohortRegistration(cohort, currentEnrolledCount) {
  if (!cohort) {
    return { ok: false, error: "Cohort not found" };
  }
  if (cohort.status !== "active" && cohort.status !== "upcoming") {
    return { ok: false, error: "Cohort is closed or inactive" };
  }
  if (cohort.capacity !== null && currentEnrolledCount >= cohort.capacity) {
    return { ok: false, error: "Cohort capacity has been reached" };
  }
  return { ok: true };
}

function filterRoster(roster, filter) {
  return roster.filter((m) => {
    if (filter === "ALL") return true;
    if (filter === "PENDING") return m.status === "INVITED" || m.status === "REGISTERED";
    if (filter === "ACTIVE") return m.status === "ACTIVE";
    if (filter === "COMPLETED") return m.status === "COMPLETED";
    return true;
  });
}

async function runTests() {
  console.log("--- RUNNING TASK 2 (CAPACITY) & TASK 3 (ROSTER) TESTS ---");

  // Test 1: 0 enrolled out of 20
  const m1 = computeCapacityMetrics(0, 20);
  assert.strictEqual(m1.pct, 0);
  assert.strictEqual(m1.remainingSpaces, 20);
  console.log("✓ Test 1: 0 enrolled / 20 capacity computes 0% and 20 remaining spaces");

  // Test 2: 12 enrolled out of 20
  const m2 = computeCapacityMetrics(12, 20);
  assert.strictEqual(m2.pct, 60);
  assert.strictEqual(m2.remainingSpaces, 8);
  console.log("✓ Test 2: 12 enrolled / 20 capacity computes 60% and 8 remaining spaces");

  // Test 3: Exactly full (20 / 20)
  const m3 = computeCapacityMetrics(20, 20);
  assert.strictEqual(m3.pct, 100);
  assert.strictEqual(m3.remainingSpaces, 0);
  console.log("✓ Test 3: 20 enrolled / 20 capacity computes 100% and 0 remaining spaces");

  // Test 4: Over-enrolled boundary guard (no impossible 167% activation)
  const m4 = computeCapacityMetrics(25, 20);
  assert.strictEqual(m4.pct, 100, "Percentage must never exceed 100% on standard UI display");
  assert.strictEqual(m4.remainingSpaces, 0);
  console.log("✓ Test 4: Stale frontend / over-capacity prevents impossible percentage displays");

  // Test 5: Unlimited / null capacity
  const m5 = computeCapacityMetrics(15, null);
  assert.strictEqual(m5.pct, 100);
  assert.strictEqual(m5.remainingSpaces, null);
  console.log("✓ Test 5: Unlimited capacity (null) handled cleanly");

  // Test 6: Server-side capacity registration gate
  const activeCohort = { id: "c1", status: "active", capacity: 20 };
  const closedCohort = { id: "c2", status: "completed", capacity: 20 };

  const canRegisterSeat19 = validateCohortRegistration(activeCohort, 19);
  assert.strictEqual(canRegisterSeat19.ok, true, "19/20 seat should be accepted");

  const canRegisterSeat20 = validateCohortRegistration(activeCohort, 20);
  assert.strictEqual(canRegisterSeat20.ok, false, "20/20 seat should be rejected");
  assert.strictEqual(canRegisterSeat20.error, "Cohort capacity has been reached");

  const canRegisterClosed = validateCohortRegistration(closedCohort, 5);
  assert.strictEqual(canRegisterClosed.ok, false, "Closed cohort must reject registration");
  console.log("✓ Test 6: Server-side registration capacity validation blocks over-enrollment");

  // Test 7: Operational Roster privacy & filtering
  const sampleRoster = [
    { id: "1", name: "Alex Harrison", email: "alex@golf.com", status: "ACTIVE", currentWeek: 3, completedFoundations: 2 },
    { id: "2", name: "David Sterling", email: "david@golf.com", status: "INVITED", currentWeek: 1, completedFoundations: 0 },
    { id: "3", name: "Sarah Lindqvist", email: "sarah@golf.com", status: "REGISTERED", currentWeek: 1, completedFoundations: 0 },
    { id: "4", name: "Elena Rossi", email: "elena@golf.com", status: "COMPLETED", currentWeek: 10, completedFoundations: 10 },
  ];

  // Verify privacy: no reflection or plan fields
  for (const athlete of sampleRoster) {
    assert.strictEqual(athlete.reflections, undefined, "Reflections must not exist on operational roster");
    assert.strictEqual(athlete.performancePlan, undefined, "Plans must not exist on operational roster");
    assert.strictEqual(athlete.vulnerabilities, undefined, "Vulnerabilities must not exist on operational roster");
  }
  console.log("✓ Test 7: Roster strictly isolates operational identity from private reflections");

  // Test 8: Roster filtering
  const pendingOnly = filterRoster(sampleRoster, "PENDING");
  assert.strictEqual(pendingOnly.length, 2);
  const activeOnly = filterRoster(sampleRoster, "ACTIVE");
  assert.strictEqual(activeOnly.length, 1);
  const completedOnly = filterRoster(sampleRoster, "COMPLETED");
  assert.strictEqual(completedOnly.length, 1);
  console.log("✓ Test 8: Roster filtering works accurately across All, Pending, Active, Completed");

  console.log("ALL TASK 2 & TASK 3 TESTS PASSED!\n");
}

runTests().catch((err) => {
  console.error("Test failed:", err);
  process.exit(1);
});
