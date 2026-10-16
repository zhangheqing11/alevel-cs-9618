def test_initial_state(sol):
    """B1: fixed-size array and empty-stack pointer on fresh module load."""
    assert sol.top_pointer == -1
    assert sol.stack == [""] * 8


def test_push_and_pop(sol):
    """B2-B3: push successive positions, then remove in last-in-first-out order."""
    for item in ["A", "B", "C"]:
        assert sol.push(item) is True
    assert sol.top_pointer == 2
    assert sol.stack[:3] == ["A", "B", "C"]
    assert sol.pop() == "C"
    assert sol.pop() == "B"
    assert sol.top_pointer == 0


def test_full(sol):
    """B4: eight successful pushes, then failed push leaves array and pointer unchanged."""
    for number in range(1, 9):
        assert sol.push(str(number)) is True
    assert sol.top_pointer == 7
    assert sol.stack == [str(number) for number in range(1, 9)]
    assert sol.push("9") is False
    assert sol.top_pointer == 7
    assert sol.stack == [str(number) for number in range(1, 9)]


def test_empty(sol):
    """B5: empty pop returns the sentinel and keeps the empty pointer."""
    assert sol.pop() == ""
    assert sol.top_pointer == -1


def test_reuse(sol):
    """B6: popped slot is reused, then stack drains and handles an extra pop."""
    assert sol.push("A") is True
    assert sol.push("B") is True
    assert sol.pop() == "B"
    assert sol.push("X") is True
    assert sol.stack[:2] == ["A", "X"]
    assert [sol.pop(), sol.pop(), sol.pop()] == ["X", "A", ""]
