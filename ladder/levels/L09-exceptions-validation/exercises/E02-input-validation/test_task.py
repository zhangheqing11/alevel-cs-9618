import pytest
from testkit import feed_input, output_lines


@pytest.mark.parametrize("answers, expected, invalid", [
    (["ABC"], "ABC", 0), (["AB", "abc", "A1C", "ZZZ"], "ZZZ", 3),
    (["ABCD", "XYZ"], "XYZ", 1),
])
def test_input_name(sol, monkeypatch, capsys, answers, expected, invalid):
    """B1-B3, B8: name length/case/letters checked until valid, with exact error messages."""
    feed_input(monkeypatch, *answers)
    result = sol.InputName()
    assert result == expected
    assert type(result) is str
    assert output_lines(capsys.readouterr().out) == ["Invalid name"] * invalid


@pytest.mark.parametrize("answers, expected, invalid", [
    (["500"], 500, 0), (["abc", "1001", "-1", "7.5", "0"], 0, 4),
    (["1000"], 1000, 0), (["", "12"], 12, 1),
])
def test_input_score(sol, monkeypatch, capsys, answers, expected, invalid):
    """B4-B8: score conversion, range and empty-input errors, independent retry loop and int result."""
    feed_input(monkeypatch, *answers)
    result = sol.InputScore()
    assert result == expected
    assert type(result) is int
    assert output_lines(capsys.readouterr().out) == ["Invalid score"] * invalid
