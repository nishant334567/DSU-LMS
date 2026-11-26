export async function fetchDashboard(studentId, signal) {
  const response = await fetch(
    `/api/v1/students/${encodeURIComponent(studentId)}/dashboard`,
    { signal },
  );

  if (!response.ok) {
    if (response.status === 404) {
      throw new Error("Student not found. Check the ID and try again.");
    }
    throw new Error("Could not load your dashboard. Please try again.");
  }

  return response.json();
}
