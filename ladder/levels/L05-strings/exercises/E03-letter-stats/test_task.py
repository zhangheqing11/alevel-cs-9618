import pytest


@pytest.mark.parametrize("text, expected", [
    ("Hello, World!", (3, 7, 3)),
    ("", (0, 0, 0)),
    ("AEIOUaeiou", (10, 0, 0)),
    ("xyz123", (0, 3, 3)),
    ("Y", (0, 1, 0)),
    (" ", (0, 0, 1)),
    ("Programming 101", (3, 8, 4)),
])
def test_letter_stats(sol, text, expected):
    """B1-B7: ASCII letters of both cases, other characters, empty/single strings."""
    result = sol.letter_stats(text)
    assert result == expected
    assert type(result) is tuple
    assert len(result) == 3
    assert all(type(value) is int for value in result)
