from testkit import output_lines


def assert_empty_state(sol):
    assert sol.ListPointer == [1, 2, 3, 4, 5, -1]
    assert sol.ListData == [""] * 6
    assert sol.StartPointer == -1
    assert sol.FreePointer == 0


def test_initialise_and_empty_output(sol, capsys):
    """B1-B2: initialise the free chain, then output the empty-list message."""
    sol.InitialiseList()
    assert_empty_state(sol)
    sol.OutputList()
    assert output_lines(capsys.readouterr().out) == ["Empty list"]


def test_insert_and_output(sol, capsys):
    """B3-B4: consume free nodes, link newest at the head and output pointer order."""
    sol.InitialiseList()
    for item in ["A", "B", "C"]:
        assert sol.InsertAtStart(item) is True
    assert sol.ListData[:3] == ["A", "B", "C"]
    assert sol.ListPointer[:3] == [-1, 0, 1]
    assert sol.StartPointer == 2
    assert sol.FreePointer == 3
    sol.OutputList()
    assert output_lines(capsys.readouterr().out) == ["C", "B", "A"]


def test_full(sol):
    """B5: six successful inserts exhaust the free list; seventh is rejected."""
    sol.InitialiseList()
    for number in range(6):
        assert sol.InsertAtStart(str(number)) is True
    assert sol.InsertAtStart("extra") is False
    assert sol.FreePointer == -1


def test_reinitialise(sol):
    """B6: reinitialisation clears both stored data and active/free pointers."""
    sol.InitialiseList()
    assert sol.InsertAtStart("A") is True
    assert sol.InsertAtStart("B") is True
    sol.InitialiseList()
    assert_empty_state(sol)
