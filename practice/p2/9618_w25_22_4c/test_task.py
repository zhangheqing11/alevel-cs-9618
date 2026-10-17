import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("score", list(range(-1,37)))
def test_range_and_existing_lookup(sol, score):
    """9618_w25_22:4(c) MP1–MP4: guard 0..35 then return the indexed BOOLEAN."""
    expected = score in {3*easy + 5*hard for easy in range(6) for hard in range(5)}
    result = sol.ValidateScore(score)
    assert type(result) is bool
    assert result is expected
