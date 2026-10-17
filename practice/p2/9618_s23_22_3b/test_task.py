import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("capacity", [0,1,3,5])
def test_eof_or_full_and_given_module(sol, tmp_path, monkeypatch, capacity):
    """9618_s23_22:3(b) MP1–MP5: process lines, stop on failed add or EOF."""
    monkeypatch.chdir(tmp_path)
    Path("queue.txt").write_text("red\n\nblue")
    sol.FileName = "queue.txt"
    values = []
    full_reported = False
    def add(value):
        nonlocal full_reported
        assert not full_reported, "Must end after AddToQueue returns False"
        if len(values) == capacity:
            full_reported = True
            return False
        values.append(value)
        return True
    monkeypatch.setattr(sol, "AddToQueue", add)
    handles = watch_open(monkeypatch)
    sol.FileToQueue()
    assert values == ["red", "", "blue"][:capacity]
    assert handles and all(h.closed for h in handles)
