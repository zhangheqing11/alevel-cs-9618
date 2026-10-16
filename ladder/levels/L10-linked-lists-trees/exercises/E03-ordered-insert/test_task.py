from testkit import output_lines


def insert_four(sol):
    for item in ["M", "C", "X", "A"]:
        assert sol.InsertInOrder(item) is True
    assert sol.ListData[:4] == ["M", "C", "X", "A"]
    assert sol.ListPointer[:4] == [2, 0, -1, 1]
    assert sol.StartPointer == 3
    assert sol.FreePointer == 4


def test_empty_insert(sol):
    """B1: first allocated node becomes the sole head, next free node is 1."""
    sol.InitialiseList()
    assert sol.InsertInOrder("M") is True
    assert sol.StartPointer == 0
    assert sol.ListPointer[0] == -1
    assert sol.FreePointer == 1


def test_order(sol, capsys):
    """B2-B3: insert before/between/after nodes and output ascending pointer order."""
    sol.InitialiseList()
    insert_four(sol)
    sol.OutputList()
    assert output_lines(capsys.readouterr().out) == ["A", "C", "M", "X"]


def test_equal_after_existing(sol, capsys):
    """B4: equal data is linked after the existing equal node, preserving successors."""
    sol.InitialiseList()
    insert_four(sol)
    assert sol.InsertInOrder("C") is True
    assert sol.ListPointer[1] == 4
    assert sol.ListPointer[4] == 0
    sol.OutputList()
    assert output_lines(capsys.readouterr().out) == ["A", "C", "C", "M", "X"]


def test_full(sol, capsys):
    """B5: repeated head insertion fills the list, rejects seventh and preserves sorted data."""
    sol.InitialiseList()
    for item in ["F", "E", "D", "C", "B", "A"]:
        assert sol.InsertInOrder(item) is True
    assert sol.InsertInOrder("Z") is False
    # Validate the finite path before asking a faulty candidate to output it.
    current = sol.StartPointer
    seen = set()
    while current != -1:
        assert 0 <= current < 6 and current not in seen
        seen.add(current)
        current = sol.ListPointer[current]
    sol.OutputList()
    assert output_lines(capsys.readouterr().out) == ["A", "B", "C", "D", "E", "F"]
