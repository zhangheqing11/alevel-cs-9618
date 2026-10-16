import pytest

A = [3, 8, 15, 22, 41, 56, 70, 89]


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


class ReadCountList(list):
    def __init__(self, values):
        super().__init__(values)
        self.reads = 0

    def __getitem__(self, index):
        self.reads += 1
        return super().__getitem__(index)


@pytest.mark.parametrize("values, target, expected", [
    (A, 22, 3), (A, 41, 4), (A, 3, 0), (A, 89, 7),
    (A, 1, -1), (A, 100, -1), (A, 50, -1), ([], 5, -1), ([7], 7, 0),
])
def test_iterative(sol, values, target, expected):
    """B1-B4: middle/end points, missing values, empty and singleton arrays."""
    assert sol.BinarySearch(values[:], target) == expected


@pytest.mark.parametrize("target, expected", [(3, 0), (89, 7), (22, 3), (1, -1), (100, -1)])
def test_recursive_values(sol, target, expected):
    """B5: recursive search succeeds on both ends/interior and rejects outside values."""
    assert sol.RecursiveBinarySearch(A[:], target, 0, 7) == expected


def test_empty_recursive_range(sol):
    """B6: empty bounds return -1 before accessing any array element."""
    assert sol.RecursiveBinarySearch([], 5, 0, -1) == -1


@pytest.mark.parametrize("recursive, target, expected", [(False, 2046, 1023), (False, 1, -1), (True, 2046, 1023)])
def test_read_bound(sol, recursive, target, expected):
    """B7: each fresh 1024-element search reads at most 50 elements and returns the right result."""
    values = ReadCountList(range(0, 2048, 2))
    if recursive:
        result = sol.RecursiveBinarySearch(values, target, 0, 1023)
    else:
        result = sol.BinarySearch(values, target)
    assert result == expected
    assert values.reads <= 50


def test_recursion(sol, monkeypatch):
    """B8: recursive search calls its module-level name more than once, wrapper restored."""
    result, calls = call_counted(sol, monkeypatch, "RecursiveBinarySearch", A[:], 89, 0, 7)
    assert result == 7
    assert calls >= 2
