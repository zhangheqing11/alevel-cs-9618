from datetime import date


def day_index(d: date) -> int:
    return d.isoweekday() % 7 + 1


def set_date(day: int, month: int, year: int) -> date:
    return date(year, month, day)


def date_to_string(d: date) -> str:
    return f"{d.day:02d}/{d.month:02d}/{d.year:04d}"


def is_weekend(d: date) -> bool:
    return day_index(d) in (1, 7)
