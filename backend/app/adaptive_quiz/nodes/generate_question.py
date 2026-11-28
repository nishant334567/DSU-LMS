"""Question-generation node for the adaptive quiz workflow."""

from typing import Any

from app.adaptive_quiz.state import AdaptiveQuizState


async def generate_question(state: AdaptiveQuizState) -> dict[str, Any]:
    """Request a question matching the current topic and difficulty."""
    # TODO: Delegate to QuestionGenerationService backed by the approved
    # question source; do not generate or persist questions in this node.
    return {}
