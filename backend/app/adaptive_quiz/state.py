"""Typed state passed between adaptive quiz workflow nodes."""

from typing import Any, Literal, NotRequired, TypedDict


class AdaptiveQuizState(TypedDict):
    """State carried through one adaptive quiz session."""

    student_id: str
    session_id: str
    course_id: str
    topic_id: str
    maximum_questions: int
    course_name: NotRequired[str]
    topic_name: NotRequired[str]
    student_metadata: NotRequired[dict[str, Any]]
    mastery_probability: NotRequired[float]
    bkt_parameters: NotRequired[dict[str, float]]
    current_difficulty: NotRequired[str]
    current_question: NotRequired[dict[str, Any]]
    question_id: NotRequired[str]
    student_answer: NotRequired[str]
    is_correct: NotRequired[bool]
    explanation: NotRequired[str]
    question_count: NotRequired[int]
    session_status: NotRequired[Literal["in_progress", "completed", "error"]]
    next_action: NotRequired[Literal["continue", "complete", "error"]]
    error: NotRequired[str]
    question_is_valid: NotRequired[bool]
    question_validation_attempts: NotRequired[int]
