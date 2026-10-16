from datetime import date
import pytest


@pytest.mark.parametrize("day, expected", [
    (date(2023, 5, 9), 3), (date(2027, 5, 2), 1), (date(2027, 5, 8), 7),
    (date(2027, 5, 3), 2), (date(2026, 10, 16), 6),
])
def test_day_index(sol, day, expected):
    """B1-B3, B9: insert weekday numbering, including Sunday/Saturday boundaries."""
    result = sol.day_index(day)
    assert result == expected
    assert type(result) is int


def test_set_date(sol):
    """B4, B9: insert parameter order and a datetime.date result."""
    result = sol.set_date(26, 10, 2003)
    assert result == date(2003, 10, 26)
    assert type(result) is date


@pytest.mark.parametrize("day, expected", [
    (date(2003, 10, 4), "04/10/2003"),
    (date(2027, 1, 5), "05/01/2027"),
    (date(2027, 12, 31), "31/12/2027"),
])
def test_date_to_string(sol, day, expected):
    """B5-B7, B9: day/month leading zeros and fixed DD/MM/YYYY string."""
    result = sol.date_to_string(day)
    assert result == expected
    assert type(result) is str


@pytest.mark.parametrize("day, expected", [
    (date(2027, 5, 2), True), (date(2027, 5, 8), True), (date(2027, 5, 3), False),
])
def test_is_weekend(sol, day, expected):
    """B8-B9: Saturday/Sunday are weekends and Monday is not; return bool."""
    assert sol.is_weekend(day) is expected
