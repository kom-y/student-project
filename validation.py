def validate_name(name: str) -> bool:
    return isinstance(name, str) and bool(name.strip()) and len(name.strip()) <= 80

def validate_marks(marks) -> bool:
    if isinstance(marks, bool):
        return False
    try:
        value = float(marks)
    except (TypeError, ValueError):
        return False
    return 0 <= value <= 100

def require_valid_name(name: str) -> str:
    if not validate_name(name):
        raise ValueError("Student name must be 1–80 non-empty characters.")
    return name.strip()

def require_valid_marks(marks) -> float:
    if not validate_marks(marks):
        raise ValueError("Marks must be a number between 0 and 100.")
    return float(marks)
