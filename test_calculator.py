import pytest
from student_app.services.calculator import calculate_grade, calculate_percentage

@pytest.mark.parametrize(("marks", "expected"), [
    (85, "A"), (75, "B"), (65, "C"), (55, "D"), (40, "F"),
    (100, "A"), (0, "F"), (84.99, "B")
])
def test_calculate_grade(marks, expected):
    assert calculate_grade(marks) == expected

@pytest.mark.parametrize("marks", [-1, 101])
def test_grade_rejects_out_of_range_marks(marks):
    with pytest.raises(ValueError):
        calculate_grade(marks)

def test_grade_rejects_non_numeric_marks():
    with pytest.raises(TypeError):
        calculate_grade("eighty")

def test_calculate_percentage():
    assert calculate_percentage(85) == 85.0
