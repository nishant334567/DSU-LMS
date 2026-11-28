"""Difficulty-selection node for the adaptive quiz workflow."""

from typing import Any

from app.adaptive_quiz.state import AdaptiveQuizState


async def select_difficulty(state: AdaptiveQuizState) -> dict[str, Any]:
    """Choose a question difficulty for the current topic."""
    # TODO: Select difficulty from the persisted mastery estimate and the
    # configured BKT parameters once the adaptive policy is implemented.
    return {}
