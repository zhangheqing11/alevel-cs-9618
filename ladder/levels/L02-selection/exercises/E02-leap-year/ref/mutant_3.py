# M3: intentional fault described in spec.md.
def is_leap(year: int) -> bool:
    return "TRUE" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "FALSE"
