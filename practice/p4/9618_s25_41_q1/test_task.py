"""9618_s25_41 Q1 circular queue; tail means last stored item."""
import re
from testkit import output_lines, run_script


def test_1a_initial_state(sol):
    """9618_s25_41:1(a) MP1-MP2: twenty -1 entries, pointers -1, count zero."""
    assert isinstance(sol.Queue, list) and sol.Queue == [-1] * 20
    assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (-1, -1, 0)


def test_1b_enqueue_full(sol):
    """9618_s25_41:1(b) MP1-MP6: first insertion, pointer and count, full failure."""
    for i in range(20):
        assert sol.Enqueue(i + 1) is True
        assert sol.Queue[i] == i + 1
        assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (0, i, i + 1)
    before = sol.Queue[:]
    assert sol.Enqueue(21) is False and sol.Queue == before
    assert sol.NumberItems == 20


def test_1bd_wrap_partial_dequeue_and_refill(sol):
    """9618_s25_41:1(b) MP4-MP6; 1(d) MP2-MP5: wrap while queue remains nonempty."""
    for i in range(1, 21):
        sol.Enqueue(i)
    for i in range(1, 8):
        assert sol.Dequeue() == i
    for i in range(21, 28):
        assert sol.Enqueue(i) is True
    assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (7, 6, 20)
    for i in range(8, 28):
        assert sol.Dequeue() == i
    assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (-1, -1, 0)


def test_1d_empty_reset_and_reuse(sol):
    """9618_s25_41:1(d) MP1/MP5/MP6: last deletion resets both pointers, next insert works."""
    assert sol.Dequeue() == -1
    for i in range(3):
        assert sol.Enqueue(i + 1) is True and sol.Dequeue() == i + 1
        assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (-1, -1, 0)
        assert sol.Dequeue() == -1


def test_1ce_screenshot(candidate_path):
    """9618_s25_41:1(c) MP1-MP3; 1(e)(i) MP1-MP2; 1(e)(ii) whole."""
    r = run_script(candidate_path)
    assert r.returncode == 0, r.stderr
    lines = output_lines(r.stdout)
    assert len(lines) == 27
    for i, line in enumerate(lines[:25], 1):
        match = re.search(r'\b(\d+)\s+(Successful|Unsuccessful)\b', line)
        assert match and int(match[1]) == i
        assert match[2] == ('Successful' if i <= 20 else 'Unsuccessful')
    assert re.search(r'\b1\b', lines[-2]) and re.search(r'\b2\b', lines[-1])
