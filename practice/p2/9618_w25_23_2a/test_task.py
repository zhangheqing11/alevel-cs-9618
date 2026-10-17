import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

def test_append_nonempty_elements_including_whitespace(sol, tmp_path, monkeypatch):
    """9618_w25_23:2(a) MP1–MP7: append, all 65 indices, empty vs whitespace, close."""
    monkeypatch.chdir(tmp_path)
    Path("data.txt").write_text("existing\n")
    sol.FileName = "data.txt"
    sol.Data = [""]*65
    sol.Data[0],sol.Data[10],sol.Data[64] = "first"," ","last"
    handles = watch_open(monkeypatch)
    sol.main()
    assert Path("data.txt").read_text() == "existing\nfirst\n \nlast\n"
    assert handles and all(h.closed for h in handles)


def test_all_empty_preserves_existing_file(sol, tmp_path, monkeypatch):
    """9618_w25_23:2(a) MP1,MP4,MP7: no nonempty elements, existing data unchanged."""
    monkeypatch.chdir(tmp_path)
    Path("data.txt").write_text("existing\n")
    sol.FileName = "data.txt"
    sol.Data = [""]*65
    sol.main()
    assert Path("data.txt").read_text() == "existing\n"
