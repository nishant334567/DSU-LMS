from datetime import date
from typing import Literal

from pydantic import Field

from app.schemas.base import IdentifiedDocument, Identifier


class Course(IdentifiedDocument):
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    department: str = Field(min_length=1)
    semester: int = Field(ge=1)
    credits: int = Field(gt=0)
    faculty_id: Identifier
    topics: list[str]


class Enrollment(IdentifiedDocument):
    student_id: Identifier
    course_id: Identifier
    academic_year: str = Field(min_length=1)
    semester: int = Field(ge=1)
    section: str = Field(min_length=1)
    status: str = Field(min_length=1)


class Attendance(IdentifiedDocument):
    student_id: Identifier
    course_id: Identifier
    date: date
    status: Literal["present", "absent"]
    session_type: str = Field(min_length=1)
