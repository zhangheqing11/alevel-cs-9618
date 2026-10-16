# M2: intentional fault described in spec.md.
def grade(mark: int) -> str:
    if mark < 0 or mark > 100:
        return "Invalid"
    if mark >= 40:
        return "E"
    elif mark >= 50:
        return "D"
    elif mark >= 60:
        return "C"
    elif mark >= 70:
        return "B"
    elif mark >= 80:
        return "A"
    return "U"
