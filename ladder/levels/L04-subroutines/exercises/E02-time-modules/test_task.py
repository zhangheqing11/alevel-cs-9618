import pytest
from testkit import output_lines


@pytest.mark.parametrize("hours, minutes, expected", [(2, 15, 135), (0, 0, 0), (0, 59, 59)])
def test_to_minutes(sol, hours, minutes, expected):
    """B1, B8: convert durations and return an integer."""
    result = sol.to_minutes(hours, minutes)
    assert result == expected
    assert type(result) is int


@pytest.mark.parametrize("total, expected", [(135, (2, 15)), (59, (0, 59)), (60, (1, 0)), (0, (0, 0))])
def test_split(sol, total, expected):
    """B2-B3, B8: return the hours/minutes tuple at conversion boundaries."""
    result = sol.split_minutes(total)
    assert result == expected
    assert type(result) is tuple
    assert all(type(value) is int for value in result)


@pytest.mark.parametrize("values, expected", [
    ((1, 50, 2, 15), "Total: 4 h 5 min"),
    ((0, 30, 0, 30), "Total: 1 h 0 min"),
    ((0, 0, 0, 0), "Total: 0 h 0 min"),
    ((10, 5, 0, 55), "Total: 11 h 0 min"),
])
def test_add_durations(sol, capsys, values, expected):
    """B4-B8: add durations with carrying, print one line and return None."""
    assert sol.add_durations(*values) is None
    assert output_lines(capsys.readouterr().out) == [expected]
