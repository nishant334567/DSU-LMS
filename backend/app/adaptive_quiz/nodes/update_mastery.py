"""Mastery-update and session-progress node for the adaptive quiz workflow."""

from typing import Any

from app.adaptive_quiz.state import AdaptiveQuizState


async def update_mastery(state: AdaptiveQuizState) -> dict[str, Any]:
    """Prepare a mastery update and determine whether the quiz should continue."""
    if state.get("session_status") == "error":
        return {"next_action": "error"}

    # TODO: Delegate mastery changes to BKTService using persisted response data.
    question_count = state.get("question_count", 0) + 1
    is_complete = question_count >= state["maximum_questions"]
    return {
        "question_count": question_count,
        "session_status": "completed" if is_complete else "in_progress",
        "next_action": "complete" if is_complete else "continue",
    }
