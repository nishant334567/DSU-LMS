"""Answer-evaluation node for the adaptive quiz workflow."""

from typing import Any

from app.adaptive_quiz.state import AdaptiveQuizState


async def evaluate_answer(state: AdaptiveQuizState) -> dict[str, Any]:
    """Evaluate the student's answer without assuming a scoring policy."""
    # TODO: Delegate to AnswerEvaluationService and return correctness and
    # feedback once the evaluation implementation is approved.
    return {}
