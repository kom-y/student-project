from student_app.models.student import Student
from student_app.services.calculator import calculate_percentage

def generate_student_report(student: Student) -> str:
    percentage = calculate_percentage(student.marks)
    return (
        "STUDENT REPORT\n"
        "--------------\n"
        f"ID: {student.student_id}\n"
        f"Name: {student.name}\n"
        f"Program: {student.program}\n"
        f"Semester: {student.semester}\n"
        f"Marks: {student.marks:g}/100\n"
        f"Percentage: {percentage:.2f}%\n"
        f"Grade: {student.grade}\n"
        f"Status: {student.status}"
    )
