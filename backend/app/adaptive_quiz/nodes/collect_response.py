"""Student-response collection node for the adaptive quiz workflow."""

from typing import Any

from langgraph.types import interrupt

from app.adaptive_quiz.state import AdaptiveQuizState


async def collect_student_response(state: AdaptiveQuizState) -> dict[str, Any]:
    """Pause the graph until the student submits an answer."""
    question_id = state.get("question_id")
    if not question_id:
        return {
            "session_status": "error",
            "next_action": "error",
            "error": "Cannot collect an answer without a question identifier",
        }

    response = interrupt(
        {
            "question_id": question_id,
            "question": state.get("current_question"),
        }
    )
    if not isinstance(response, dict) or response.get("question_id") != question_id:
        return {
            "session_status": "error",
            "next_action": "error",
            "error": "Resumed answer does not match the current question",
        }

    student_answer = response.get("student_answer")
    if not isinstance(student_answer, str):
        return {
            "session_status": "error",
            "next_action": "error",
            "error": "Resumed answer must be a string",
        }

    # TODO: Apply answer-format and session-ownership checks at the API boundary.
    return {"student_answer": student_answer}
