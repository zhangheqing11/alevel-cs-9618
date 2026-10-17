import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("records", [[("AB1234","Freddie Jones","FreddieJ909@Cambridge.org")],[("AB1234","Freddie Jones","FreddieJ909@Cambridge.org"),("BC2345","Sue Smith","Sue1024@Cambridge.org")]])
def test_three_lines_to_backslash_record(sol, tmp_path, monkeypatch, records):
    """9618_w25_22:3(a) MP1–MP6: QP data, field order, backslashes, repeated triples."""
    monkeypatch.chdir(tmp_path)
    text = "\n".join(item for row in records for item in row)
    Path("OldFile.txt").write_text(text)
    Path("NewFile.txt").write_text("obsolete\n")
    handles = watch_open(monkeypatch)
    sol.main()
    assert Path("NewFile.txt").read_text() == "".join("\\".join(row)+"\n" for row in records)
    assert Path("OldFile.txt").read_text() == text
    assert handles and all(h.closed for h in handles)
