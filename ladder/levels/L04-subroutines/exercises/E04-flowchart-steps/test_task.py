import pytest
from testkit import feed_input, output_lines


@pytest.mark.parametrize("number, expected", [(6, 8), (1, 0), (2, 1), (16, 4), (7, 16), (27, 111)])
def test_steps(sol, monkeypatch, capsys, number, expected):
    """B1-B6: flowchart's pre-condition loop and joined counter update."""
    feed_input(monkeypatch, str(number))
    sol.count_steps()
    assert output_lines(capsys.readouterr().out) == [f"Steps: {expected}"]
