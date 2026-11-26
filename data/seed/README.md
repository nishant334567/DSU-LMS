# LENA synthetic seed data

All records are fictional and created for development/demo use. They do not represent actual DSU students, faculty, course codes, or official academic records.

## Files
- students.json: 5 synthetic B.Tech CSE students
- faculty.json: fictional faculty profiles
- courses.json: sample semester 4 courses
- enrollments.json: student-course relationships
- attendance.json: dated lecture attendance records
- assessments.json: quizzes, assignment and midterm metadata
- quiz_attempts.json: student quiz outcomes and topic scores
- assessment_results.json: student marks linked to assessments and courses
- learning_resources.json: course resource metadata (PDF paths are placeholders)
- activity_events.json: sample learning engagement events

## Assessment results
- assessment_results.json contains 25 fictional results: one per existing student and assessment.
- Each result references an existing student, course, and assessment; quiz marks match quiz_attempts.json.
- Assignment marks are provisional and pending publication; quiz and midterm results are published.
- Results are linked by student_id, course_id, and assessment_id. They do not create new students, courses, or assessments.

## Notes
- IDs are consistent across files.
- Dates and marks are synthetic.
- PDF paths are placeholders; add your own course material at those paths or update the metadata.
- The data is intentionally small and suitable for a prototype, not production analytics.
