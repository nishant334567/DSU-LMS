from datetime import datetime
from typing import Optional

from pydantic import Field

from app.schemas.base import IdentifiedDocument, Identifier


class LearningResource(IdentifiedDocument):
    course_id: Identifier
    title: str = Field(min_length=1)
    type: str = Field(min_length=1)
    topic: str = Field(min_length=1)
    difficulty: str = Field(min_length=1)
    file_path: str = Field(min_length=1)
    tags: list[str]


class ActivityEvent(IdentifiedDocument):
    student_id: Identifier
    course_id: Identifier
    event_type: str = Field(min_length=1)
    resource_id: Optional[Identifier]
    duration_seconds: Optional[int] = Field(ge=0)
    timestamp: datetime
