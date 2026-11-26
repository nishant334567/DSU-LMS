"use client";

import { useEffect, useRef, useState } from "react";
import { CoursePerformance, Improvement, Overview, RecentActivity, UpcomingAssessments, Welcome } from "../components/DashboardSections";
import { LoadingState } from "../components/ui";
import { fetchDashboard } from "../lib/api";

export default function DashboardPage() {
  const [studentId, setStudentId] = useState("");
  const [dashboard, setDashboard] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const request = useRef(null);

  useEffect(() => () => request.current?.abort(), []);

  async function handleSubmit(event) {
    event.preventDefault();
    const id = studentId.trim();
    if (!id) {
      request.current?.abort();
      setLoading(false);
      setDashboard(null);
      setError("Enter your student ID to view your dashboard.");
      return;
    }

    request.current?.abort();
    const controller = new AbortController();
    request.current = controller;
    setError("");
    setDashboard(null);
    setLoading(true);

    try {
      const data = await fetchDashboard(id, controller.signal);
      if (!controller.signal.aborted) setDashboard(data);
    } catch (error) {
      if (!controller.signal.aborted) {
        setError(error instanceof TypeError ? "Can't reach the dashboard service. Check that the backend is running." : error.message);
      }
    } finally {
      if (!controller.signal.aborted) setLoading(false);
    }
  }

  return (
    <div className="app-shell">
      <header className="site-header">
        <div className="header-inner">
          <a className="brand" href="/" aria-label="LENA home">
            <span className="brand-mark" aria-hidden="true">✳</span>
            <span>LENA<small>LEARNING ASSISTANT</small></span>
          </a>
          <span className="header-label"><span className="header-label-dot" /> STUDENT DASHBOARD</span>
          <span className="header-school">DSU <span>·</span> Student space</span>
        </div>
      </header>

      <main className="main-content">
        <div className="page-top">
          <div>
            <p className="breadcrumb">MY LEARNING <span>/</span> DASHBOARD</p>
            <p className="page-kicker">Your learning, all in one place.</p>
          </div>
          <form className="student-form" onSubmit={handleSubmit}>
            <label htmlFor="student-id">Student ID</label>
            <div className="input-group">
              <input id="student-id" value={studentId} onChange={(event) => setStudentId(event.target.value)} placeholder="Enter your student ID" autoComplete="off" />
              <button type="submit">{loading ? "Loading…" : "View dashboard"} <span aria-hidden="true">↗</span></button>
            </div>
          </form>
        </div>

        {error && <div className="notice error-notice" role="alert">{error}</div>}
        {loading && <LoadingState />}
        {!dashboard && !loading && !error && (
          <section className="welcome welcome-empty">
            <div>
              <p className="eyebrow welcome-eyebrow">WELCOME TO LENA</p>
              <h1>Your learning, <br />in focus<span className="welcome-dot">.</span></h1>
              <p>Enter your student ID above to see your progress, courses, and what&apos;s coming up.</p>
              <span className="welcome-tag">A little progress, every day <span aria-hidden="true">✳</span></span>
            </div>
            <div className="welcome-art" aria-hidden="true"><div className="art-orbit orbit-one" /><div className="art-orbit orbit-two" /><div className="art-center">✳</div></div>
          </section>
        )}
        {dashboard && (
          <>
            <Welcome student={dashboard.student} />
            <Overview attendance={dashboard.overall_attendance_percentage} courses={dashboard.enrolled_courses} performance={dashboard.course_performance} />
            <div className="dashboard-grid">
              <div className="dashboard-column"><CoursePerformance courses={dashboard.course_performance} /><RecentActivity events={dashboard.recent_learning_activity} /></div>
              <div className="dashboard-column"><UpcomingAssessments assessments={dashboard.upcoming_assessments} /><Improvement /></div>
            </div>
          </>
        )}
      </main>
      <footer className="footer"><span>LENA <span className="footer-dot">✳</span> Learning Experience &amp; Nurturing Agent</span><span>Made for curious minds.</span></footer>
    </div>
  );
}
