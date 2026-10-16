from datetime import date


def day_index(d: date) -> int:
    """Like DAYINDEX(): Sunday = 1, Monday = 2, ..., Saturday = 7."""
    raise NotImplementedError


def set_date(day: int, month: int, year: int) -> date:
    """Like SETDATE(Day, Month, Year): note the parameter order."""
    raise NotImplementedError


def date_to_string(d: date) -> str:
    """Return 'DD/MM/YYYY' with leading zeros for day and month."""
    raise NotImplementedError


def is_weekend(d: date) -> bool:
    """Return True for Saturday or Sunday."""
    raise NotImplementedError
