from dataclasses import dataclass

@dataclass
class Student:
    student_id: str
    name: str
    program: str
    semester: int
    marks: float

    @property
    def grade(self) -> str:
        from student_app.services.calculator import calculate_grade
        return calculate_grade(self.marks)

    @property
    def status(self) -> str:
        return "Pass" if self.marks >= 50 else "Needs Improvement"
