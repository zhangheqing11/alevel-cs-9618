import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("text,values", [("first\n\nthird",["first","","third"]),("single\n",["single"]),("",[])])
def test_copy_each_line_into_next_element(sol, tmp_path, monkeypatch, text, values):
    """9618_s24_23:2(a) MP1–MP6: EOF, blank lines, consecutive indices, close."""
    monkeypatch.chdir(tmp_path)
    Path("data.txt").write_text(text)
    sol.FileName = "data.txt"
    sol.Data = ["sentinel"] * (len(values)+2)
    handles = watch_open(monkeypatch)
    sol.main()
    assert sol.Data[:len(values)] == values
    assert handles and all(h.closed for h in handles)
