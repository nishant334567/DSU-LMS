import { formatDate, formatEvent, formatPercentage, overallPerformance } from "../lib/format";
import { Badge, Card, EmptyState, SectionHeader, Stat } from "./ui";

export function Welcome({ student }) {
  const firstName = student.name?.trim().split(/\s+/)[0] || "student";
  return (
    <section className="welcome">
      <div>
        <p className="eyebrow welcome-eyebrow">YOUR LEARNING SPACE</p>
        <h1>Welcome back, {firstName}<span className="welcome-dot">.</span></h1>
        <p>A little progress every day adds up. Here&apos;s where your learning stands.</p>
        <div className="profile-details">
          <span>{student.program}</span>
          <span className="profile-divider" aria-hidden="true" />
          <span>Semester {student.semester}</span>
          <span className="profile-divider" aria-hidden="true" />
          <span>{student.department}</span>
        </div>
      </div>
      <div className="welcome-art" aria-hidden="true">
        <div className="art-orbit orbit-one" />
        <div className="art-orbit orbit-two" />
        <div className="art-center">✳</div>
        <span className="art-sparkle sparkle-one">✦</span>
        <span className="art-sparkle sparkle-two">✦</span>
      </div>
    </section>
  );
}

export function Overview({ attendance, courses, performance }) {
  return (
    <section className="overview" aria-label="Overview statistics">
      <Stat label="Overall attendance" value={formatPercentage(attendance)} detail="Across recorded sessions" icon="◷" />
      <Stat label="Enrolled courses" value={courses.length} detail="Your active courses" icon="▤" />
      <Stat label="Assessment performance" value={formatPercentage(overallPerformance(performance))} detail="Based on published marks" icon="↗" />
    </section>
  );
}

export function CoursePerformance({ courses }) {
  return (
    <Card className="performance-card">
      <SectionHeader eyebrow="YOUR PROGRESS" title="Course performance" description="A snapshot of your published assessment results." aside={<span className="header-symbol" aria-hidden="true">↗</span>} />
      {courses.length === 0 ? <EmptyState>No course performance available yet.</EmptyState> : (
        <div className="course-list">
          {courses.map((course) => (
            <div className="course-row" key={course.course_id}>
              <div className="course-info">
                <div>
                  <p className="course-name">{course.course_name}</p>
                  <span className="course-code">{course.course_id} · {course.max_marks ? `${course.marks_obtained} / ${course.max_marks} marks` : "No published results"}</span>
                </div>
                <strong className="course-score">{formatPercentage(course.percentage)}</strong>
              </div>
              {course.percentage != null && (
                <div className="progress-track" role="progressbar" aria-label={`${course.course_name} performance`} aria-valuenow={course.percentage} aria-valuemin="0" aria-valuemax="100">
                  <span style={{ width: `${Math.min(100, Math.max(0, course.percentage))}%` }} />
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}

export function UpcomingAssessments({ assessments }) {
  return (
    <Card>
      <SectionHeader eyebrow="WHAT'S NEXT" title="Upcoming assessments" description="Keep an eye on what’s ahead." />
      {assessments.length === 0 ? <EmptyState>No upcoming assessments right now.</EmptyState> : (
        <div className="item-list">
          {assessments.map((assessment) => (
            <div className="assessment-item" key={assessment.assessment_id}>
              <span className="item-icon calendar-icon" aria-hidden="true">▦</span>
              <div className="item-copy">
                <p className="item-title">{assessment.title}</p>
                <p className="item-meta">{assessment.course_name} · {formatDate(assessment.due_at || assessment.scheduled_at)}</p>
              </div>
              <Badge>{assessment.type}</Badge>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}

export function Improvement() {
  return (
    <Card className="improvement-card">
      <SectionHeader eyebrow="ROOM TO GROW" title="Areas for improvement" />
      <div className="improvement-content">
        <span className="improvement-icon" aria-hidden="true">✦</span>
        <div>
          <p className="item-title">Insights coming soon</p>
          <p className="item-meta">Topic-level insights aren&apos;t available in your dashboard data yet.</p>
        </div>
      </div>
    </Card>
  );
}

export function RecentActivity({ events }) {
  return (
    <Card>
      <SectionHeader eyebrow="YOUR LEARNING JOURNEY" title="Recent activity" description="The latest steps in your learning." />
      {events.length === 0 ? <EmptyState>No recent learning activity yet.</EmptyState> : (
        <div className="item-list activity-list">
          {events.map((event) => (
            <div className="activity-item" key={event.event_id}>
              <span className="activity-dot" aria-hidden="true" />
              <div className="item-copy">
                <p className="item-title activity-title">{formatEvent(event.event_type)}</p>
                <p className="item-meta">{event.resource_title || event.course_name || event.course_id}</p>
              </div>
              <span className="activity-date">{formatDate(event.timestamp)}</span>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}
