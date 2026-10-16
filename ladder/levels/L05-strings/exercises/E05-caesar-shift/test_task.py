import pytest


@pytest.mark.parametrize("text, shift, expected", [
    ("ABC", 1, "BCD"), ("XYZ", 3, "ABC"),
    ("Hello, World!", 13, "Uryyb, Jbeyq!"), ("abc", 0, "abc"),
    ("", 5, ""), ("Zz", 1, "Aa"), ("a-z", 25, "z-y"),
])
def test_caesar_shift(sol, text, shift, expected):
    """B1-B7: ordinary/zero/max shifts, case-specific wrapping and unchanged punctuation."""
    assert sol.caesar_shift(text, shift) == expected
