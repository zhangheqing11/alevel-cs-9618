import pytest


@pytest.mark.parametrize("file_name, expected", [
    ("program1.txt", 5), ("comments.txt", 0), ("empty.txt", 0), ("trailing.txt", 2),
])
def test_count_code_lines(sol, file_name, expected):
    """B1-B5: skip blank/space/comment lines, keep inline comments and last unterminated line."""
    result = sol.count_code_lines(file_name)
    assert result == expected
    assert type(result) is int
