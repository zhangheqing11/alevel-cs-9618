import pytest


def call_counted(sol, monkeypatch, name, *args):
    original = getattr(sol, name)
    calls = 0

    def wrapper(*values):
        nonlocal calls
        calls += 1
        return original(*values)

    with monkeypatch.context() as patch:
        patch.setattr(sol, name, wrapper)
        result = getattr(sol, name)(*args)
    return result, calls


@pytest.mark.parametrize("name, argument, expected", [
    ("Factorial", 0, 1), ("Factorial", 1, 1), ("Factorial", 5, 120), ("Factorial", 10, 3628800),
    ("SumDigits", 0, 0), ("SumDigits", 7, 7), ("SumDigits", 1234, 10),
    ("SumDigits", 9999, 36), ("SumDigits", 1000, 1),
    ("Reverse", "", ""), ("Reverse", "a", "a"), ("Reverse", "abc", "cba"),
    ("Reverse", "Hello", "olleH"), ("Reverse", "racecar", "racecar"),
])
def test_values(sol, name, argument, expected):
    """B1-B6: basic/ordinary cases for factorial, digits (including zeroes) and strings."""
    assert getattr(sol, name)(argument) == expected


@pytest.mark.parametrize("name, argument, expected", [
    ("Factorial", 5, 120), ("SumDigits", 1234, 10), ("Reverse", "abc", "cba"),
])
def test_recursion(sol, monkeypatch, name, argument, expected):
    """B7: each function uses its own name recursively, with correct result."""
    result, calls = call_counted(sol, monkeypatch, name, argument)
    assert result == expected
    assert calls >= 2
