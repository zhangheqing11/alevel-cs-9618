from testkit import output_lines

EXPECTED = ["8", "Comter", "pu", "COMPUTER", "rtpo", "2", "p", "16!"]


def test_prediction(sol):
    """B1: hand-worked prediction is the complete list of eight strings."""
    assert sol.PREDICTED == EXPECTED


def test_trace(sol, capsys):
    """B2-B6: concatenation, one-based MID, reverse stride and character codes."""
    sol.run_trace()
    assert output_lines(capsys.readouterr().out) == EXPECTED
