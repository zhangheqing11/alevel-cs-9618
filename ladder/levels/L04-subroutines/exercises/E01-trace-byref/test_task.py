from testkit import output_lines

EXPECTED = ["In AddOne: 4", "A: 3", "A: 8 B: 3", "A: 18"]


def test_prediction(sol):
    """B1: hand-worked prediction includes all four output strings."""
    assert sol.PREDICTED == EXPECTED


def test_trace(sol, capsys):
    """B2-B4: complete trace, unchanged BYVAL argument and swapped BYREF values."""
    sol.run_trace()
    assert output_lines(capsys.readouterr().out) == EXPECTED


def test_helpers(sol, capsys):
    """B5-B7: swapped tuple, twice including negatives, and printing procedure."""
    assert sol.swap(1, 2) == (2, 1)
    assert sol.swap(5, 5) == (5, 5)
    for value, expected in [(5, 10), (0, 0), (-4, -8)]:
        assert sol.twice(value) == expected
    assert sol.add_one(5) is None
    assert output_lines(capsys.readouterr().out) == ["In AddOne: 6"]
