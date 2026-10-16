import pytest

@pytest.mark.parametrize(
    'year, expected',
    [
        (2024, True),
        (2023, False),
        (1900, False),
        (2100, False),
        (2000, True),
        (2400, True),
        (4, True),
        (1, False),
    ],
)
def test_leap_year(sol, year, expected):
    """B1-B6: MOD rule, century exceptions and bool return."""
    result = sol.is_leap(year)
    assert result is expected
    assert type(result) is bool
