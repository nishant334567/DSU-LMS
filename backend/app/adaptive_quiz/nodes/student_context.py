"""Student-context node for the adaptive quiz workflow."""

from typing import Any

from app.adaptive_quiz.state import AdaptiveQuizState
from app.database.json_data import get_record_by_id


def load_student_context(state: AdaptiveQuizState) -> dict[str, Any]:
    """Load the student's seed record into workflow state."""
    student = get_record_by_id("students.json", state["student_id"])
    if student is None:
        return {
            "session_status": "error",
            "next_action": "error",
            "error": f"Student {state['student_id']} not found",
        }

    # TODO: Enrich context from course/topic records and replace JSON access
    # with the planned persistence integration when it is implemented.
    return {"student_metadata": student}
