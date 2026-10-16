from testkit import output_lines


def test_prediction(sol):
    """B1: exact three-line hand prediction."""
    assert sol.PREDICTED == ["4 5", "9", "6 9"]


def test_trace(sol, capsys):
    """B2: independent counters and overridden Increment give the complete output."""
    sol.RunTrace()
    assert output_lines(capsys.readouterr().out) == ["4 5", "9", "6 9"]


def test_limited_counter(sol):
    """B3: checking the limit before adding allows 6 to become 9, then stops."""
    counter = sol.LimitedCounter(3, 7)
    for _ in range(4):
        counter.Increment()
    assert counter.GetCount() == 9


def test_inheritance_and_private_fields(sol):
    """B4: inheritance and exactly the parent/child private attributes."""
    assert issubclass(sol.LimitedCounter, sol.Counter)
    assert set(vars(sol.LimitedCounter(3, 7))) == {"_Counter__Count", "_Counter__StepSize", "_LimitedCounter__Limit"}


def test_counter(sol):
    """B5: parent Increment uses the supplied step on every call."""
    counter = sol.Counter(4)
    for _ in range(3):
        counter.Increment()
    assert counter.GetCount() == 12
