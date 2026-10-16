from testkit import output_lines

EXPECTED = ["7 6", "Student1: 10", "Student2: 11", "Student3: 10"]


def test_prediction(sol):
    """B1: hand-worked prediction describes copying rather than aliasing."""
    assert sol.PREDICTED == EXPECTED


def test_trace(sol, capsys):
    """B2-B4: record copy and separately constructed array records give all four lines."""
    sol.run_trace()
    assert output_lines(capsys.readouterr().out) == EXPECTED


def test_pupil_defaults(sol):
    """B5: both fields of a new PupilRecord have their required defaults."""
    pupil = sol.PupilRecord()
    assert pupil.last_name == ""
    assert pupil.year_group == 0
