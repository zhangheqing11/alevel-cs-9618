from pathlib import Path
from testkit import output_lines

FILE_LINES = ["1: APPLE", "2: BANANA", "3: CHERRY", "4: DATE"]
OUTPUT = ["Lines written: 4", "Blank lines: 2"]


def test_prediction(sol):
    """B1-B2: predict both the written file and the screen totals."""
    assert sol.PREDICTED_FILE == FILE_LINES
    assert sol.PREDICTED_OUTPUT == OUTPUT


def test_trace(sol, capsys):
    """B3-B5: overwrite old content, skip blank lines, number output, preserve input."""
    original = Path("words.txt").read_bytes()
    sol.run_trace()
    assert Path("out.txt").read_text(encoding="utf-8").splitlines() == FILE_LINES
    assert output_lines(capsys.readouterr().out) == OUTPUT
    assert Path("words.txt").read_bytes() == original
