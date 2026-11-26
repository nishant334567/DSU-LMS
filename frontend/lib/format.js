export function formatPercentage(value) {
  return value == null ? "—" : `${Number(value.toFixed(2))}%`;
}

export function overallPerformance(courses) {
  const totals = courses.reduce(
    (sum, course) => ({
      obtained: sum.obtained + course.marks_obtained,
      maximum: sum.maximum + course.max_marks,
    }),
    { obtained: 0, maximum: 0 },
  );
  return totals.maximum ? (totals.obtained / totals.maximum) * 100 : null;
}

export function formatDate(value) {
  if (!value) return "Date unavailable";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "Date unavailable";
  return new Intl.DateTimeFormat("en-IN", {
    day: "numeric",
    month: "short",
    year: "numeric",
    timeZone: "Asia/Kolkata",
  }).format(date);
}

export function formatEvent(value) {
  return value.replaceAll("_", " ");
}
