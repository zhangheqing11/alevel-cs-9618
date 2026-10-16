def test_initial_state(sol):
    """B1: queue storage, pointers and count start at the specified initial state."""
    assert (sol.front_pointer, sol.rear_pointer, sol.number_of_items) == (0, -1, 0)
    assert sol.queue == [""] * 5


def test_fifo(sol):
    """B2: three enqueues followed by two dequeues demonstrate first-in-first-out."""
    for item in ["A", "B", "C"]:
        assert sol.enqueue(item) is True
    assert [sol.dequeue(), sol.dequeue()] == ["A", "B"]
    assert sol.number_of_items == 1


def test_full(sol):
    """B3: five slots can be filled; the sixth item is rejected without replacing data."""
    for item in ["A", "B", "C", "D", "E"]:
        assert sol.enqueue(item) is True
    assert sol.enqueue("F") is False
    assert sol.queue == ["A", "B", "C", "D", "E"]


def test_wraparound(sol):
    """B4-B5: reuse two freed slots, wrap rear and front, drain, then return empty sentinel."""
    for item in ["A", "B", "C", "D", "E"]:
        assert sol.enqueue(item) is True
    assert [sol.dequeue(), sol.dequeue()] == ["A", "B"]
    assert sol.enqueue("F") is True
    assert sol.enqueue("G") is True
    assert sol.rear_pointer == 1
    assert sol.queue == ["F", "G", "C", "D", "E"]
    assert [sol.dequeue() for _ in range(6)] == ["C", "D", "E", "F", "G", ""]
    assert sol.front_pointer == 2
    assert sol.number_of_items == 0


def test_empty(sol):
    """B6: empty dequeue leaves both pointers and count unchanged."""
    before = (sol.front_pointer, sol.rear_pointer, sol.number_of_items)
    assert sol.dequeue() == ""
    assert (sol.front_pointer, sol.rear_pointer, sol.number_of_items) == before
