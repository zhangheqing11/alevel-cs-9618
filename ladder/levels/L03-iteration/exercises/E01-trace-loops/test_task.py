from testkit import output_lines

EXPECTED = ["A: 22", "B: 5", "C: 10", "D: 5", "D: 3", "D: 1", "F: done"]


def test_predicted(sol):
    """B1: store the seven hand-worked output strings in PREDICTED."""
    assert sol.PREDICTED == EXPECTED


def test_translated_trace(sol, capsys):
    """B2-B6: inclusive FOR, post-condition loop, negative STEP and no E line."""
    sol.run_trace()
    lines = output_lines(capsys.readouterr().out)
    assert lines == EXPECTED
