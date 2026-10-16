import pytest


@pytest.mark.parametrize("code, expected", [
    ("AB123", True), ("ZZ000", True), ("ab123", False),
    ("A1234", False), ("AB12C", False), ("AB12", False),
    ("AB1234", False), ("", False), ("AB1.5", False),
    ("AB-12", False), ("AB 23", False),
])
def test_valid_code(sol, code, expected):
    """B1-B7: exact format/length, case, character positions and digits, Boolean result."""
    result = sol.ValidCode(code)
    assert result is expected
    assert type(result) is bool
