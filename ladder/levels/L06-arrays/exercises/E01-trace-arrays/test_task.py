from testkit import output_lines

EXPECTED = ["4 25", "0 1 16", "4 99", "23 12"]


def test_prediction(sol):
    """B1: hand-worked prediction is all four output strings."""
    assert sol.PREDICTED == EXPECTED


def test_trace(sol, capsys):
    """B2-B5: backwards shift, independent copy/rows and correct 2D indexing."""
    sol.run_trace()
    assert output_lines(capsys.readouterr().out) == EXPECTED
