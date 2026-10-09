def calculate_grade(marks: float) -> str:
    """Return a grade using the Week 01 thresholds."""
    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        raise TypeError("Marks must be a number.")
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 85:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 65:
        return "C"
    if marks >= 55:
        return "D"
    return "F"

def calculate_percentage(marks: float, total: float = 100) -> float:
    if total <= 0:
        raise ValueError("Total marks must be greater than zero.")
    if not 0 <= marks <= total:
        raise ValueError("Marks must be between zero and total.")
    return round((marks / total) * 100, 2)
