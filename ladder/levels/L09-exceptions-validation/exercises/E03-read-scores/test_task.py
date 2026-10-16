from testkit import output_lines


def test_initial_state(sol):
    """B1: twenty actual integer slots and zero initial count."""
    assert sol.ScoreArray == [-1] * 20
    assert sol.NumberScores == 0


def test_read_scores(sol, capsys):
    """B2-B4: preserve valid-line order, unused slots, skip bad lines and ignore blanks."""
    assert sol.ReadScores("Scores.txt") == 4
    assert sol.NumberScores == 4
    assert sol.ScoreArray == [120, 85, 300, 42] + [-1] * 16
    assert output_lines(capsys.readouterr().out) == ["Skipped: abc", "Skipped: 7.5"]


def test_missing(sol, capsys):
    """B5: report a missing file without exception or array changes."""
    assert sol.ReadScores("Nope.txt") == 0
    assert sol.NumberScores == 0
    assert sol.ScoreArray == [-1] * 20
    assert output_lines(capsys.readouterr().out) == ["File not found"]


def test_read_twice(sol):
    """B6: each call resets the count and fills from the start again."""
    assert sol.ReadScores("Scores.txt") == 4
    assert sol.ReadScores("Scores.txt") == 4
    assert sol.NumberScores == 4
    assert sol.ScoreArray[:5] == [120, 85, 300, 42, -1]
