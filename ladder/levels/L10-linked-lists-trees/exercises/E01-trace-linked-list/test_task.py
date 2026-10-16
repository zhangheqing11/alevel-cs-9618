from testkit import output_lines

EXPECTED = ["Ant Bee Cat Dog", "Elk Ant Bee Cat Dog", "Free: 5"]


def test_prediction(sol):
    """B1: predicted lines match, allowing trailing spaces as specified."""
    assert [line.rstrip() for line in sol.PREDICTED] == EXPECTED


def test_trace(sol, capsys):
    """B2-B5: pointer order before/after head insertion and next free node."""
    sol.RunTrace()
    assert output_lines(capsys.readouterr().out) == EXPECTED
