import pytest


@pytest.mark.parametrize("text, expected", [
    ("  IF X > 13 THEN  ", "IF X > 13 THEN"),
    ("abc", "abc"), ("   ", ""), ("", ""),
    (" a b ", "a b"), ("a", "a"), ("  x", "x"), ("x  ", "x"),
])
def test_trim_spaces(sol, text, expected):
    """B1-B7: trim each edge, preserve middle spaces, handle empty/all-space strings."""
    assert sol.trim_spaces(text) == expected
