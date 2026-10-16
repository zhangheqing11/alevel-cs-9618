import pytest


@pytest.mark.parametrize("rolls, expected", [
    ([1, 6, 6, 3], [1, 0, 1, 0, 0, 2]),
    ([], [0, 0, 0, 0, 0, 0]),
    ([6, 6, 6, 6, 6], [0, 0, 0, 0, 0, 5]),
    ([1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 1, 1]),
])
def test_tally(sol, rolls, expected):
    """B1-B3, B7: six integer counters including absent faces and highest index."""
    result = sol.tally(rolls)
    assert result == expected
    assert type(result) is list
    assert len(result) == 6
    assert all(type(value) is int for value in result)


@pytest.mark.parametrize("rolls, expected", [
    ([1, 6, 6, 3], 6), ([2, 2, 5, 5], 2),
    ([1, 2, 3, 4, 5, 6], 1), ([4], 4), ([], 0),
])
def test_most_frequent(sol, rolls, expected):
    """B4-B7: return the face, smallest on ties, zero for no rolls; integer result."""
    result = sol.most_frequent(rolls)
    assert result == expected
    assert type(result) is int
