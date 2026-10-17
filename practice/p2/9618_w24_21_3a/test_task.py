import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("text,expected", [("first\nsecond\nthird",["first","second","third"]),("old\nolder\nlast A\n\nlast C\n",["last A","","last C"])])
def test_last_three_lines_same_order_and_close(sol, tmp_path, monkeypatch, capsys, text, expected):
    """9618_w24_21:3(a) MP1–MP4: completed EOF loop/read/close around given shifts."""
    monkeypatch.chdir(tmp_path)
    Path("Result.txt").write_text(text)
    handles = watch_open(monkeypatch)
    sol.main()
    assert capsys.readouterr().out.splitlines() == expected
    assert handles and all(h.closed for h in handles)
    assert Path("Result.txt").read_text() == text
