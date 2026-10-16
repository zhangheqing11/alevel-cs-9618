import pytest


def walk(sol):
    current = sol.StartPointer
    seen = set()
    values = []
    while current != -1:
        assert 0 <= current < 6 and current not in seen
        seen.add(current)
        values.append(sol.ListData[current])
        current = sol.ListPointer[current]
    return values


@pytest.mark.parametrize("item, result, pointers, start, free, values", [
    ("A", True, [2, 0, -1, 4, 5, -1], 1, 3, ["C", "M", "X"]),
    ("M", True, [4, 2, -1, 1, 5, -1], 3, 0, ["A", "C", "X"]),
    ("X", True, [-1, 0, 4, 1, 5, -1], 3, 2, ["A", "C", "M"]),
    ("Q", False, [2, 0, -1, 1, 5, -1], 3, 4, ["A", "C", "M", "X"]),
])
def test_delete(sol, item, result, pointers, start, free, values):
    """B1-B4: delete head/middle/tail, recycle the node, or leave everything unchanged if absent."""
    sol.ListData = ["M", "C", "X", "A", "", ""]
    sol.ListPointer = [2, 0, -1, 1, 5, -1]
    sol.StartPointer, sol.FreePointer = 3, 4
    original_data = sol.ListData[:]
    assert sol.DeleteItem(item) is result
    assert sol.ListPointer == pointers
    assert (sol.StartPointer, sol.FreePointer) == (start, free)
    assert walk(sol) == values
    if not result:
        assert sol.ListData == original_data


def test_delete_only_node(sol):
    """B5: deleting the sole active node leaves an empty list and prepends it to the free chain."""
    sol.ListData = ["A", "", "", "", "", ""]
    sol.ListPointer = [-1, 2, 3, 4, 5, -1]
    sol.StartPointer, sol.FreePointer = 0, 1
    assert sol.DeleteItem("A") is True
    assert sol.ListPointer == [1, 2, 3, 4, 5, -1]
    assert sol.StartPointer == -1
    assert sol.FreePointer == 0
    assert walk(sol) == []
