# M3: intentional fault described in spec.md.
def grade(mark: int) -> str:
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    elif mark >= 40:
        return "E"
    return "U"
