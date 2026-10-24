"""9618_s22_42 Q1 stack; MS accepts uncleared or cleared popped slots."""
import re
from testkit import run_script


def nums(text):
    return [int(x) for x in re.findall(r'-?\d+', text)]


def test_1a_declarations(sol):
    """9618_s22_42:1(a) MP1-MP3: array and next-free pointer."""
    assert isinstance(sol.StackData, list) and len(sol.StackData) == 10
    assert sol.StackPointer == 0


def test_1b_printarray(sol, capsys):
    """9618_s22_42:1(b) MP2-MP3: all ten elements and pointer, in either order."""
    sol.StackData = list(range(11, 21)); sol.StackPointer = 4
    sol.PrintArray()
    out = nums(capsys.readouterr().out)
    assert out == [4] + list(range(11, 21)) or out == list(range(11, 21)) + [4]


def test_1c_push_boundary(sol):
    """9618_s22_42:1(c) MP2-MP6: ten additions, full rejects without changing data."""
    for i in range(10):
        assert sol.Push(11 + i) is True
        assert sol.StackPointer == i + 1 and sol.StackData[i] == 11 + i
    before = sol.StackData[:]
    assert sol.Push(21) is False
    assert sol.StackPointer == 10 and sol.StackData == before


def test_1e_pop_lifo_empty_reuse(sol):
    """9618_s22_42:1(e)(i) MP1-MP5: numeric return, LIFO, empty sentinel, slot reuse."""
    assert sol.Pop() == -1 and sol.StackPointer == 0
    for v in [3, 7, 0, -6]:
        sol.Push(v)
    for remaining, expected in [(3, -6), (2, 0), (1, 7), (0, 3)]:
        assert sol.Pop() == expected and sol.StackPointer == remaining
    assert sol.Pop() == -1
    assert sol.Push(42) is True and sol.Pop() == 42


def test_1d_screenshot(candidate_path):
    """9618_s22_42:1(d)(i) MP1-MP5; 1(d)(ii) whole: first ten stored, eleventh rejected."""
    r = run_script(candidate_path, stdin='\n'.join(map(str, range(11, 22))) + '\n')
    assert r.returncode == 0, r.stderr
    lines = [x.strip() for x in r.stdout.splitlines() if x.strip()]
    assert len(lines) >= 11
    statuses = [x.rsplit(':', 1)[-1].strip() for x in lines[:11]]
    assert len(set(statuses[:10])) == 1 and statuses[10] != statuses[0]
    out = nums('\n'.join(lines[11:]))
    assert out[:11] == [10] + list(range(11, 21))


def test_1e_screenshot_after_two_pops(candidate_path):
    """9618_s22_42:1(e)(ii) MP1-MP2: before and after output; accept all MS slot variants."""
    r = run_script(candidate_path, stdin='\n'.join(map(str, range(11, 22))) + '\n')
    assert r.returncode == 0, r.stderr
    lines = [x for x in r.stdout.splitlines() if x.strip()]
    out = nums('\n'.join(lines[11:]))
    assert out[:11] == [10] + list(range(11, 21))
    after = out[11:]
    assert after[0] == 8 and after[1:9] == list(range(11, 19))
    assert after[9:] in ([], [19, 20], [0, 0])
