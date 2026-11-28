"""Interface for future Bayesian Knowledge Tracing operations."""


class BKTService:
    """Define the async mastery operations used by the adaptive quiz workflow."""

    async def get_initial_mastery(
        self, student_id: str, topic_id: str
    ) -> tuple[float, dict[str, float]]:
        """Return initial mastery and its parameters for a student topic."""
        # TODO: Load persisted mastery and parameters; do not calculate BKT here.
        raise NotImplementedError("Initial mastery retrieval is not implemented")

    async def update_mastery(
        self,
        student_id: str,
        topic_id: str,
        mastery_probability: float,
        is_correct: bool,
        bkt_parameters: dict[str, float],
    ) -> float:
        """Return updated mastery after an answer has been evaluated."""
        # TODO: Implement BKT calculations and persistence in a separate change.
        raise NotImplementedError("Mastery updates are not implemented")
