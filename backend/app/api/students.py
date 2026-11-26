from datetime import datetime, timezone
from typing import Any, Dict

from fastapi import APIRouter, HTTPException

from app.database.json_data import filter_records, get_record_by_id, load_records


router = APIRouter(prefix="/api/v1/students", tags=["students"])


def _parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


@router.get("/{student_id}/dashboard")
def get_student_dashboard(student_id: str) -> Dict[str, Any]:
    student = get_record_by_id("students.json", student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    enrollments = [
        enrollment
        for enrollment in filter_records("enrollments.json", "student_id", student_id)
        if enrollment.get("status") == "active"
    ]
    course_ids = {enrollment["course_id"] for enrollment in enrollments}
    enrolled_courses = [
        course
        for course in load_records("courses.json")
        if course["_id"] in course_ids
    ]
    course_names = {course["_id"]: course["name"] for course in enrolled_courses}

    attendance = [
        record
        for record in filter_records("attendance.json", "student_id", student_id)
        if record.get("course_id") in course_ids
    ]
    attendance_percentage = (
        round(
            sum(record.get("status") == "present" for record in attendance)
            / len(attendance)
            * 100,
            2,
        )
        if attendance
        else None
    )

    assessments = load_records("assessments.json")
    assessments_by_id = {assessment["_id"]: assessment for assessment in assessments}
    results = [
        result
        for result in filter_records(
            "assessment_results.json", "student_id", student_id
        )
        if result.get("result_status") == "published"
        and result.get("course_id") in course_ids
    ]
    course_performance = []
    for course in enrolled_courses:
        course_results = [
            result for result in results if result["course_id"] == course["_id"]
        ]
        total_marks = sum(result["marks_obtained"] for result in course_results)
        max_marks = sum(result["max_marks"] for result in course_results)
        course_performance.append(
            {
                "course_id": course["_id"],
                "course_name": course["name"],
                "marks_obtained": total_marks,
                "max_marks": max_marks,
                "percentage": (
                    round(total_marks / max_marks * 100, 2) if max_marks else None
                ),
                "assessments": [
                    {
                        "assessment_id": result["assessment_id"],
                        "title": assessments_by_id[result["assessment_id"]]["title"],
                        "type": assessments_by_id[result["assessment_id"]]["type"],
                        "marks_obtained": result["marks_obtained"],
                        "max_marks": result["max_marks"],
                        "percentage": result["percentage"],
                    }
                    for result in course_results
                ],
            }
        )

    now = datetime.now(timezone.utc)
    upcoming_assessments = []
    for assessment in assessments:
        course_id = assessment.get("course_id")
        date_field = "due_at" if "due_at" in assessment else "scheduled_at"
        date_value = assessment.get(date_field)
        if course_id in course_ids and date_value:
            if _parse_timestamp(date_value) > now:
                upcoming_assessments.append(
                    {
                        "assessment_id": assessment["_id"],
                        "title": assessment["title"],
                        "type": assessment["type"],
                        "course_id": course_id,
                        "course_name": course_names[course_id],
                        date_field: date_value,
                    }
                )
    upcoming_assessments.sort(
        key=lambda assessment: _parse_timestamp(
            assessment.get("due_at", assessment.get("scheduled_at"))
        )
    )

    resources = {
        resource["_id"]: resource
        for resource in load_records("learning_resources.json")
    }
    recent_activity = filter_records("activity_events.json", "student_id", student_id)
    recent_activity.sort(
        key=lambda event: _parse_timestamp(event["timestamp"]), reverse=True
    )

    return {
        "student": student,
        "enrolled_courses": enrolled_courses,
        "overall_attendance_percentage": attendance_percentage,
        "course_performance": course_performance,
        "upcoming_assessments": upcoming_assessments,
        "recent_learning_activity": [
            {
                "event_id": event["_id"],
                "event_type": event["event_type"],
                "course_id": event["course_id"],
                "course_name": course_names.get(event["course_id"]),
                "resource_id": event["resource_id"],
                "resource_title": resources.get(event["resource_id"], {}).get("title"),
                "duration_seconds": event["duration_seconds"],
                "timestamp": event["timestamp"],
            }
            for event in recent_activity[:5]
        ],
    }
