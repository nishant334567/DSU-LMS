"""Interface for future adaptive question retrieval or generation."""

from typing import Any


class QuestionGenerationService:
    """Define the async question-generation operation for the quiz workflow."""

    async def generate_question(
        self, course_id: str, topic_id: str, difficulty: str
    ) -> dict[str, Any]:
        """Return a question matching the requested course, topic, and level."""
        # TODO: Connect an approved question source; do not integrate an LLM here.
        raise NotImplementedError("Question generation is not implemented")
