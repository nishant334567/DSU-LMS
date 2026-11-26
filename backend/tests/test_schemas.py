import unittest
from datetime import date, datetime

from pydantic import ValidationError

from app.database.json_data import load_records
from app.schemas.academic import Attendance, Course, Enrollment
from app.schemas.assessments import Assessment, AssessmentResult, QuizAttempt
from app.schemas.learning import ActivityEvent, LearningResource
from app.schemas.people import Faculty, Student


COLLECTIONS = {
    "students.json": Student,
    "faculty.json": Faculty,
    "courses.json": Course,
    "enrollments.json": Enrollment,
    "attendance.json": Attendance,
    "assessments.json": Assessment,
    "assessment_results.json": AssessmentResult,
    "quiz_attempts.json": QuizAttempt,
    "learning_resources.json": LearningResource,
    "activity_events.json": ActivityEvent,
}


class SchemaTests(unittest.TestCase):
    def test_seed_documents_validate_and_preserve_field_names(self):
        for filename, model in COLLECTIONS.items():
            for record in load_records(filename):
                record_id = record.get("_id", record.get("result_id"))
                with self.subTest(filename=filename, record=record_id):
                    document = model.model_validate(record)
                    self.assertEqual(
                        set(document.model_dump(by_alias=True, exclude_unset=True)),
                        set(record),
                    )

    def test_id_alias_and_dates(self):
        student = Student.model_validate(load_records("students.json")[0])
        self.assertEqual(student.id, student.model_dump(by_alias=True)["_id"])
        self.assertIsInstance(
            Attendance.model_validate(load_records("attendance.json")[0]).date, date
        )
        self.assertIsInstance(
            QuizAttempt.model_validate(load_records("quiz_attempts.json")[0]).attempted_at,
            datetime,
        )
        result = AssessmentResult.model_validate(load_records("assessment_results.json")[0])
        self.assertNotIn("_id", result.model_dump(by_alias=True))

    def test_invalid_result_and_quiz_marks_are_rejected(self):
        result = load_records("assessment_results.json")[0]
        with self.assertRaises(ValidationError):
            AssessmentResult.model_validate({**result, "marks_obtained": result["max_marks"] + 1})
        with self.assertRaises(ValidationError):
            AssessmentResult.model_validate({**result, "result_status": "pending"})
        with self.assertRaises(ValidationError):
            AssessmentResult.model_validate({**result, "percentage": 101})
        attempt = load_records("quiz_attempts.json")[0]
        with self.assertRaises(ValidationError):
            QuizAttempt.model_validate({**attempt, "score": attempt["total_marks"] + 1})


if __name__ == "__main__":
    unittest.main()
