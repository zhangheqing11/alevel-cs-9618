import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("values", [[],["one"],["PPP","NNN","ZZZ","XXX","YYY","WWW"],["a","b","c","d","e","f","g"]])
def test_write_active_stack_top_first(sol, tmp_path, monkeypatch, values):
    """9618_s23_23:3(b)(ii) MP1–MP5; both MS POP and non-POP schemes accepted."""
    monkeypatch.chdir(tmp_path)
    sol.Stack = values + ["unused"] * (7-len(values))
    sol.BottomOfStack = 500
    sol.TopOfStack = 499 + len(values)
    sol.FileName = "Stack.txt"
    Path("Stack.txt").write_text("old content\n")
    handles = watch_open(monkeypatch)
    sol.SaveStack()
    expected = "".join(value + "\n" for value in reversed(values))
    assert Path("Stack.txt").read_text() == expected
    assert handles and all(h.closed for h in handles)
