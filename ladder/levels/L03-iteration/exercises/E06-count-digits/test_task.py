import pytest


@pytest.mark.parametrize(
    "number, expected",
    [(0, 1), (7, 1), (10, 2), (99, 2), (100, 3), (123456, 6), (1000000, 7)],
)
def test_count_digits(sol, number, expected):
    """B1-B4, B8: zero, carry boundaries, large numbers and integer counts."""
    result = sol.count_digits(number)
    assert result == expected
    assert type(result) is int


@pytest.mark.parametrize(
    "number, expected",
    [(0, 0), (5, 5), (1234, 10), (9999, 36), (1000, 1), (908, 17)],
)
def test_digit_sum(sol, number, expected):
    """B5-B8: zero, ordinary digits, zero-containing values and integer sums."""
    result = sol.digit_sum(number)
    assert result == expected
    assert type(result) is int
