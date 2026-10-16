import pytest


@pytest.mark.parametrize("text, expected", [
    ("()", True), ("([]{})", True), ("{[()()]}", True),
    ("a(b[c]d)e", True), ("", True),
    ("(]", False), ("([)]", False), ("((", False), ("(", False),
    ("))", False), (")(", False),
])
def test_balanced(sol, text, expected):
    """B1-B7: match types and nesting, ignore text, check empty input/stack and leftover openers."""
    result = sol.balanced(text)
    assert result is expected
    assert type(result) is bool
