import pytest


@pytest.mark.parametrize("search_name, expected", [
    ("Cy", 88), ("Ann", 71), ("Dee", 55), ("BO", 64), ("bo", 64), ("Zed", -1),
])
def test_lookup(sol, search_name, expected):
    """B1-B5, B7: first/middle/last/absent name, case folding and first duplicate."""
    names = ["Ann", "Bo", "Cy", "bo", "Dee"]
    marks = [71, 64, 88, 90, 55]
    assert sol.look_up_mark(names, marks, search_name) == expected
    assert names == ["Ann", "Bo", "Cy", "bo", "Dee"]
    assert marks == [71, 64, 88, 90, 55]


def test_empty(sol):
    """B6: no students returns the not-found sentinel."""
    assert sol.look_up_mark([], [], "Ann") == -1
