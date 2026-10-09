import json
from pathlib import Path

from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS
from student_app.logger import get_logger
from student_app.models.student import Student
from student_app.reports.student_report import generate_student_report
from student_app.utils.validation import require_valid_name, require_valid_marks

logger = get_logger()

def load_student(path: Path) -> Student:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    name = require_valid_name(data.get("name"))
    marks = require_valid_marks(data.get("marks"))
    return Student(
        student_id=str(data.get("id", "N/A")),
        name=name,
        program=str(data.get("program", "Not specified")),
        semester=int(data.get("semester", 1)),
        marks=marks,
    )

def main() -> int:
    logger.info("Application started")
    print(f"Application: {APP_NAME}")
    print(f"Debug mode: {DEBUG}")
    print(f"Maximum students: {MAX_STUDENTS}")
    try:
        data_path = Path(__file__).resolve().parents[2] / "data" / "student.json"
        student = load_student(data_path)
        print()
        print(generate_student_report(student))
        logger.info("Student report generated for ID %s", student.student_id)
        return 0
    except (OSError, json.JSONDecodeError, ValueError, TypeError) as exc:
        logger.error("Could not process student data: %s", exc)
        print(f"Error: {exc}")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
