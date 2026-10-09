import pytest
from student_app.utils.validation import (
    validate_name, validate_marks, require_valid_name, require_valid_marks
)

@pytest.mark.parametrize("name", ["Ali", " Sara Khan ", "A"])
def test_valid_names(name):
    assert validate_name(name)

@pytest.mark.parametrize("name", ["", "   ", None, "x" * 81])
def test_invalid_names(name):
    assert not validate_name(name)

@pytest.mark.parametrize("marks", [0, 50, 100, "85.5"])
def test_valid_marks(marks):
    assert validate_marks(marks)

@pytest.mark.parametrize("marks", [-1, 101, "abc", None, True])
def test_invalid_marks(marks):
    assert not validate_marks(marks)

def test_require_valid_name_strips_spaces():
    assert require_valid_name("  Ali  ") == "Ali"

def test_require_valid_marks_converts_to_float():
    assert require_valid_marks("85") == 85.0

def test_require_valid_name_raises():
    with pytest.raises(ValueError):
        require_valid_name(" ")

def test_require_valid_marks_raises():
    with pytest.raises(ValueError):
        require_valid_marks(101)
