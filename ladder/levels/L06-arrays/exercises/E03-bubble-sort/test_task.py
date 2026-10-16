import pytest


@pytest.mark.parametrize("original_names, original_marks, expected_names, expected_marks", [
    (["Ann", "Bo", "Cy", "Dee"], [64, 88, 71, 90], ["Dee", "Bo", "Cy", "Ann"], [90, 88, 71, 64]),
    (["P", "Q", "R", "S"], [10, 20, 30, 40], ["S", "R", "Q", "P"], [40, 30, 20, 10]),
    (["A", "B", "C"], [70, 85, 70], ["B", "A", "C"], [85, 70, 70]),
    (["W", "X", "Y", "Z"], [60, 60, 60, 60], ["W", "X", "Y", "Z"], [60, 60, 60, 60]),
    (["Solo"], [50], ["Solo"], [50]), ([], [], [], []),
])
def test_sort_by_mark(sol, original_names, original_marks, expected_names, expected_marks):
    """B1-B7: descending stable order in both caller-owned lists; None return."""
    names = original_names[:]
    marks = original_marks[:]
    names_alias, marks_alias = names, marks
    assert sol.sort_by_mark(names, marks) is None
    assert names_alias == expected_names
    assert marks_alias == expected_marks
