# DSU-LMS / LENA — Next Steps

## 1. Long-term goals

Grow LENA into a personalised learning assistant that understands student progress, identifies learning gaps, adapts practice, and recommends timely support. Keep future capabilities modular so they can later be coordinated by a main LENA agent.

## 2. Short-term goals

Deliver an adaptive quiz that uses student and topic context, adjusts question difficulty based on performance, evaluates answers, updates topic mastery, and saves session results. The student should be able to complete a quiz and see the system adapt—not just receive a fixed list of questions.

## 3. Current progress

- The existing dashboard and FastAPI backend are operational and use JSON seed data.
- A LangGraph adaptive-quiz skeleton is on `main` (`b38634c`).
- The graph has workflow nodes, conditional routing, validation retries, and an interrupt/resume response node.
- BKT, question generation, and answer evaluation are placeholders. MongoDB, quiz API routes/schemas, and dashboard integration are not implemented.
- Validation retry exhaustion currently ends with an error message but does not set the session status to `error`.

## 4. Next actionable items

1. Connect the backend to MongoDB.
2. Add 10 approved sample records to MongoDB.
3. Implement the adaptive-quiz nodes and services.
4. Run and verify the first adaptive quiz end to end.

## 5. Gotchas to watch for

- Confirm what the 10 records represent; use synthetic or anonymised student data unless real-data use is authorised.
- Keep MongoDB credentials in environment variables; never commit secrets.
- Use persistent graph checkpointing if quiz sessions must survive restarts and resume later.
- Fix the validation-exhaustion status before relying on API status responses.
- Keep existing student APIs working and avoid expanding into unrelated LENA capabilities during the quiz work.