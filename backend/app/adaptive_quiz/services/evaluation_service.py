"""Interface for future student-answer evaluation."""

from typing import Any


class AnswerEvaluationService:
    """Define the async answer-evaluation operation for the quiz workflow."""

    async def evaluate_answer(
        self, question: dict[str, Any], student_answer: str
    ) -> dict[str, Any]:
        """Return correctness and feedback for an answer to a question."""
        # TODO: Implement an approved evaluation strategy without assuming
        # correctness or generating feedback in this interface.
        raise NotImplementedError("Answer evaluation is not implemented")
