import pytest


@pytest.mark.parametrize("values, index, expected", [
    ([2, 5, 8, 3, 1], 3, [2, 3, 5, 8, 1]),
    ([2, 3, 5, 8, 1], 4, [1, 2, 3, 5, 8]),
    ([1, 4, 9], 2, [1, 4, 9]), ([4, 2, 1], 0, [4, 2, 1]),
    ([5, 7, 6], 2, [5, 6, 7]),
])
def test_insert_one(sol, values, index, expected):
    """B1-B4, B8: one insertion's intermediate state, unchanged suffix, boundaries and None return."""
    array = values[:]
    alias = array
    assert sol.InsertOne(array, index) is None
    assert alias == expected


@pytest.mark.parametrize("values, expected", [
    ([45, 12, 78, 3, 33, 12], [3, 12, 12, 33, 45, 78]),
    ([], []), ([5], [5]), ([1, 2, 3], [1, 2, 3]), ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9]),
])
def test_sort(sol, values, expected):
    """B5-B6, B8: duplicates, empty/single/sorted/reverse arrays sorted in place, None return."""
    array = values[:]
    alias = array
    assert sol.InsertionSort(array) is None
    assert alias == expected


def test_calls_insert_one(sol, monkeypatch):
    """B7: five-element sort delegates at least four insertion steps to InsertOne."""
    array = [4, 3, 2, 1, 0]
    calls = 0
    original = sol.InsertOne

    def wrapper(*args):
        nonlocal calls
        calls += 1
        return original(*args)

    with monkeypatch.context() as patch:
        patch.setattr(sol, "InsertOne", wrapper)
        result = sol.InsertionSort(array)
    assert result is None
    assert array == [0, 1, 2, 3, 4]
    assert calls >= 4
