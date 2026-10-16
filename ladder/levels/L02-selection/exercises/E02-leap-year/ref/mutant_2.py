# M2: intentional fault described in spec.md.
def is_leap(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0
