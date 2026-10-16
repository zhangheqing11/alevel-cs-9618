import pytest


@pytest.mark.parametrize("text, expected", [
    ("72", 72), ("0", 0), ("100", 100), ("101", -1), ("-5", -1),
    ("abc", -1), ("", -1), ("7.5", -1), ("1e2", -1), (" 72 ", 72),
])
def test_convert_mark(sol, text, expected):
    """B1-B7: integer conversion, inclusive boundaries, invalid forms/spaces and int result."""
    result = sol.ConvertMark(text)
    assert result == expected
    assert type(result) is int
