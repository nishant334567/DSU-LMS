import assert from "node:assert/strict";
import { test } from "node:test";
import { fetchDashboard } from "./api.js";
import { formatPercentage, overallPerformance } from "./format.js";

test("performance weights published marks and handles no results", () => {
  assert.equal(overallPerformance([
    { marks_obtained: 8, max_marks: 10 },
    { marks_obtained: 30, max_marks: 50 },
  ]), 38 / 60 * 100);
  assert.equal(overallPerformance([{ marks_obtained: 0, max_marks: 0 }]), null);
  assert.equal(formatPercentage(null), "—");
  assert.equal(formatPercentage(0), "0%");
});

test("dashboard requests encode student IDs and report failures", async () => {
  const originalFetch = globalThis.fetch;
  try {
    let url;
    globalThis.fetch = async (value) => {
      url = value;
      return { ok: true, json: async () => ({ student: { name: "Test" } }) };
    };
    assert.deepEqual(await fetchDashboard("a/b"), { student: { name: "Test" } });
    assert.equal(url, "/api/v1/students/a%2Fb/dashboard");

    globalThis.fetch = async () => ({ ok: false, status: 404 });
    await assert.rejects(fetchDashboard("missing"), /Student not found/);
    globalThis.fetch = async () => ({ ok: false, status: 500 });
    await assert.rejects(fetchDashboard("id"), /Could not load/);
  } finally {
    globalThis.fetch = originalFetch;
  }
});
