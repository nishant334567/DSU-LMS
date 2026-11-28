"""Question-validation node for the adaptive quiz workflow."""

from typing import Any

from app.adaptive_quiz.state import AdaptiveQuizState


async def validate_question(state: AdaptiveQuizState) -> dict[str, Any]:
    """Check that question generation returned a question and its identifier."""
    question = state.get("current_question")
    question_id = state.get("question_id")
    is_valid = isinstance(question, dict) and bool(question) and bool(question_id)
    if is_valid:
        return {"question_is_valid": True, "question_validation_attempts": 0}

    attempts = state.get("question_validation_attempts", 0) + 1
    # TODO: Validate the complete question schema and content before presenting it.
    return {
        "question_is_valid": False,
        "question_validation_attempts": attempts,
        "error": "Generated question is missing required structure",
    }
