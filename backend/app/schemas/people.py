from pydantic import Field

from app.schemas.base import IdentifiedDocument


class Student(IdentifiedDocument):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    phone: str = Field(min_length=1)
    department: str = Field(min_length=1)
    program: str = Field(min_length=1)
    semester: int = Field(ge=1)
    section: str = Field(min_length=1)
    academic_year: str = Field(min_length=1)
    campus: str = Field(min_length=1)
    status: str = Field(min_length=1)


class Faculty(IdentifiedDocument):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    department: str = Field(min_length=1)
    designation: str = Field(min_length=1)
