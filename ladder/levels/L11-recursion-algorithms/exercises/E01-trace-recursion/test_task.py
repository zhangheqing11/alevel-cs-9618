from testkit import output_lines

EXPECTED = ["Down 3", "Down 2", "Down 1", "Go", "Up 1", "Up 2", "Up 3", "32", "1"]


def call_counted(sol, monkeypatch, name, *args):
    original = getattr(sol, name)
    calls = 0

    def wrapper(*values):
        nonlocal calls
        calls += 1
        return original(*values)

    with monkeypatch.context() as patch:
        patch.setattr(sol, name, wrapper)
        result = getattr(sol, name)(*args)
    return result, calls


def test_prediction(sol):
    """B1: all nine hand-worked lines in exact order."""
    assert sol.PREDICTED == EXPECTED


def test_trace(sol, capsys):
    """B2: winding/unwinding and power results match the full trace."""
    sol.RunTrace()
    assert output_lines(capsys.readouterr().out) == EXPECTED


def test_countdown_one(sol, capsys):
    """B3: base case lies between down and up for a single recursive level."""
    sol.Countdown(1)
    assert output_lines(capsys.readouterr().out) == ["Down 1", "Go", "Up 1"]


def test_powers(sol):
    """B4: repeated multiplication and exponent-one/zero boundaries."""
    assert sol.Power(3, 4) == 81
    assert sol.Power(5, 1) == 5
    assert sol.Power(9, 0) == 1


def test_recursive_modules(sol, monkeypatch, capsys):
    """B5: both modules actually call their own module-level names, wrappers restored afterward."""
    result, calls = call_counted(sol, monkeypatch, "Power", 2, 5)
    assert result == 32
    assert calls >= 2
    _, calls = call_counted(sol, monkeypatch, "Countdown", 3)
    assert calls >= 2
    assert output_lines(capsys.readouterr().out) == EXPECTED[:7]
