"""Exact matching w22/42 Q3 MS; corpus MP numbering."""
import re

from testkit import run_script


def test_3a_queue_and_pointers(sol):
    """9618_w22_42:3(a) MP1-MP3: fixed queue and QP pointer convention."""
    assert isinstance(sol.Queue, list) and len(sol.Queue) == 100
    assert sol.HeadPointer == -1 and sol.TailPointer == 0


def test_3b_first_last_and_full(sol):
    """9618_w22_42:3(b) MP2-MP6: writes before advancing; full failure preserves state."""
    for value in range(100):
        assert sol.Enqueue(value + 12) is True
        assert sol.Queue[value] == value + 12
        assert sol.TailPointer == value + 1 and sol.HeadPointer == 0
    before = sol.Queue.copy()
    assert sol.Enqueue(999) is False
    assert sol.Queue == before and sol.TailPointer == 100


def test_3d_recursive_sum(sol, monkeypatch):
    """9618_w22_42:3(d) MP2-MP6: recursive accumulation to start, pointer decreases."""
    sol.Queue = [8, -3, 17, 0, 9] + [12345] * 95
    sol.HeadPointer = 0
    calls = []
    original = sol.RecursiveOutput

    def spy(start):
        calls.append(start)
        return original(start)

    monkeypatch.setattr(sol, 'RecursiveOutput', spy)
    assert spy(0) == 8
    calls.clear()
    assert spy(4) == 31
    assert calls == [4, 3, 2, 1, 0]


def test_3e_ii_screenshot_total(candidate_path, exercise_dir):
    """9618_w22_42:3(c) MP1-MP4; 3(e)(i) whole; 3(e)(ii) whole: 210."""
    result = run_script(candidate_path, files_dir=exercise_dir / 'files')
    assert result.returncode == 0, result.stderr
    assert 'Successful' in result.stdout and 'Unsuccessful' not in result.stdout
    assert re.findall(r'-?\d+', result.stdout)[-1:] == ['210']
