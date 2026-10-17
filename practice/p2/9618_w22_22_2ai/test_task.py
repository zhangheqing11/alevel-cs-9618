import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

def test_35_students_append_names_only(sol, tmp_path, monkeypatch, capsys):
    """9618_w22_22:2(a)(i) MP1–MP5: exactly 35 names/marks, <20, append and close."""
    monkeypatch.chdir(tmp_path)
    Path("Support_List.txt").write_text("Previous Student\n")
    marks = [20]*35
    marks[0],marks[1],marks[2],marks[34] = 19,20,0,19
    answers = []
    for i,mark in enumerate(marks):
        answers.extend([f"Student {i+1}",str(mark)])
    feed_input(monkeypatch,*answers)
    handles = watch_open(monkeypatch)
    sol.main()
    assert Path("Support_List.txt").read_text() == "Previous Student\nStudent 1\nStudent 3\nStudent 35\n"
    assert handles and all(h.closed for h in handles)
    assert capsys.readouterr().out == ""
