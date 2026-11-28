"""Initial mastery node for the adaptive quiz workflow."""

from typing import Any

from app.adaptive_quiz.state import AdaptiveQuizState


async def initialize_mastery(state: AdaptiveQuizState) -> dict[str, Any]:
    """Prepare initial topic mastery for the quiz session."""
    # TODO: Request initial mastery from BKTService using the student's
    # persisted learning history once that integration is implemented.
    return {}
