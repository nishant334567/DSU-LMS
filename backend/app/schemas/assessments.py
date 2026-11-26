from datetime import datetime
from typing import Literal, Optional, Self

from pydantic import Field, model_validator

from app.schemas.base import IdentifiedDocument, Identifier, SeedModel


class Assessment(IdentifiedDocument):
    course_id: Identifier
    title: str = Field(min_length=1)
    type: Literal["quiz", "assignment", "midterm"]
    max_marks: int = Field(gt=0)
    scheduled_at: Optional[datetime] = None
    due_at: Optional[datetime] = None
    topic_weights: Optional[dict[str, int]] = None


class AssessmentResult(SeedModel):
    result_id: Identifier
    student_id: Identifier
    course_id: Identifier
    assessment_id: Identifier
    marks_obtained: int = Field(ge=0)
    max_marks: int = Field(gt=0)
    percentage: float = Field(ge=0, le=100)
    result_status: Literal["published", "pending"]
    published_at: Optional[datetime]

    @model_validator(mode="after")
    def validate_result(self) -> Self:
        if self.marks_obtained > self.max_marks:
            raise ValueError("marks_obtained cannot exceed max_marks")
        if (self.result_status == "published") != (self.published_at is not None):
            raise ValueError("published_at must be set only for published results")
        return self


class QuizAttempt(IdentifiedDocument):
    student_id: Identifier
    course_id: Identifier
    assessment_id: Identifier
    attempt_number: int = Field(ge=1)
    score: int = Field(ge=0)
    total_marks: int = Field(gt=0)
    percentage: float = Field(ge=0, le=100)
    topic_scores: dict[str, int]
    difficulty: str = Field(min_length=1)
    attempted_at: datetime

    @model_validator(mode="after")
    def validate_score(self) -> Self:
        if self.score > self.total_marks:
            raise ValueError("score cannot exceed total_marks")
        return self
