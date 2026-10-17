import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("values", [list(range(100,300)),list(range(-200,0)),[999]+list(range(199))])
def test_all_200_unique_values(sol, capsys, values):
    """9618_w22_21:3 MP2–MP7: first/last maxima and negative-only input."""
    sol.Data = values[:]
    sol.main()
    lines = output_lines(capsys.readouterr().out)
    assert len(lines) == 1 and int(lines[0]) == max(values)


def test_requested_search_algorithm(candidate_path):
    """9618_w22_21:3 MP3–MP6: D10 disallows built-in max as an algorithm replacement."""
    no_shortcuts(candidate_path)
