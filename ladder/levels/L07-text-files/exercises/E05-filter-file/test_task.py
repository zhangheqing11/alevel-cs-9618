from pathlib import Path
import pytest


@pytest.mark.parametrize("pass_mark, excluded, expected", [
    (40, 2, ["Ann,71", "Cy,40", "Dee,88", "Fay,100"]),
    (41, 3, ["Ann,71", "Dee,88", "Fay,100"]),
    (0, 0, ["Ann,71", "Bo,39", "Cy,40", "Dee,88", "Eve,0", "Fay,100"]),
    (100, 5, ["Fay,100"]),
])
def test_filter_marks(sol, pass_mark, excluded, expected):
    """B1-B4, B6: numeric inclusive thresholds, skip blanks, order and unchanged input."""
    original = Path("marks.txt").read_bytes()
    assert sol.filter_marks("marks.txt", "passed.txt", pass_mark) == excluded
    assert Path("passed.txt").read_text(encoding="utf-8").splitlines() == expected
    assert Path("marks.txt").read_bytes() == original


def test_overwrite(sol):
    """B5-B6: discard junk in output and preserve the original input file."""
    original = Path("marks.txt").read_bytes()
    Path("passed.txt").write_text("junk\n", encoding="utf-8")
    assert sol.filter_marks("marks.txt", "passed.txt", 40) == 2
    assert Path("passed.txt").read_text(encoding="utf-8").splitlines() == ["Ann,71", "Cy,40", "Dee,88", "Fay,100"]
    assert Path("marks.txt").read_bytes() == original
