"""9618_s22_42 Question 2 (2D array, bubble sort, recursive binary search): tests from the exact matching MS.

The main program uses random numbers, so screenshot-style tests run it through a small wrapper that
seeds `random` first (any seed must give a correct program). Grid rows are output lines holding
exactly 10 integers; the first 10 such lines are the "before" grid, the next 10 the "after" grid.
"""
import ast
import re

import pytest

from testkit import run_script

ROW = [5, 7, 10, 11, 28, 29, 47, 61, 62, 85]  # first line of the "after" grid in the MS 2(c)(ii) screenshot


def run_seeded(candidate_path, tmp_path, seed):
    wrapper = tmp_path / f"seeded_{seed}.py"
    wrapper.write_text(
        "import random, runpy, sys\n"
        f"random.seed({seed})\n"
        f"sys.argv = [{str(candidate_path)!r}]\n"
        f"runpy.run_path({str(candidate_path)!r}, run_name='__main__')\n",
        encoding="utf-8")
    return run_script(wrapper)


def ints(line):
    parts = [p for p in re.split(r"[\s,;|]+", line.strip()) if p]
    if parts and all(re.fullmatch(r"-?\d+", p) for p in parts):
        return [int(p) for p in parts]
    return None


def grids(res):
    """(before, after, tail lines after the second grid)."""
    rows, last = [], -1
    for i, ln in enumerate(res.lines):
        v = ints(ln)
        if v is not None and len(v) == 10:
            rows.append(v)
            last = i
            if len(rows) == 20:
                break
    assert len(rows) == 20, f"expected two 10 x 10 grids (20 lines of 10 values), found {len(rows)} grid lines"
    return rows[:10], rows[10:], res.lines[last + 1:]


@pytest.fixture
def seeded(candidate_path, tmp_path):
    res = run_seeded(candidate_path, tmp_path, 2022)
    assert res.returncode == 0, res.stderr[-800:]
    return res


# ---------------------------------------------------------------- 2(a)

def test_2a_ten_by_ten_random_1_to_100(seeded):
    """9618_s22_42:2(a) MP1-MP4: 10 x 10 integer array, every element random between 1 and 100."""
    before, _, _ = grids(seeded)
    for row in before:
        assert all(1 <= v <= 100 for v in row), f"value outside 1..100 in {row}"


def test_2a_values_are_random(candidate_path, tmp_path):
    """9618_s22_42:2(a) MP4: different runs give different arrays (random numbers, not fixed values)."""
    a = run_seeded(candidate_path, tmp_path, 1)
    b = run_seeded(candidate_path, tmp_path, 2)
    assert a.returncode == 0 and b.returncode == 0, (a.stderr + b.stderr)[-800:]
    assert grids(a)[0] != grids(b)[0]


# ---------------------------------------------------------------- 2(b)(i)

def _sorted_on_one_dimension(before, after):
    rows_ok = all(sorted(b) == a for b, a in zip(before, after))
    cols_b = [list(c) for c in zip(*before)]
    cols_a = [list(c) for c in zip(*after)]
    cols_ok = all(sorted(b) == a for b, a in zip(cols_b, cols_a))
    return rows_ok or cols_ok


@pytest.mark.parametrize("seed", [2022, 7, 99])
def test_2b_i_bubble_sort_each_line_ascending(candidate_path, tmp_path, seed):
    """9618_s22_42:2(b)(i) MP1-MP5: every line of the first dimension sorted ascending, same values."""
    res = run_seeded(candidate_path, tmp_path, seed)
    assert res.returncode == 0, res.stderr[-800:]
    before, after, _ = grids(res)
    assert _sorted_on_one_dimension(before, after), "after grid is not the before grid sorted ascending"


def test_2b_i_no_builtin_sort(candidate_path):
    """9618_s22_42:2(b)(i): QP 'You must not use any built-in sorting functions'."""
    tree = ast.parse(candidate_path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            name = f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else ""
            assert name not in ("sorted", "sort"), "built-in sort used (QP forbids it)"


# ---------------------------------------------------------------- 2(b)(ii) / (iii)

def test_2b_iii_screenshot_unsorted_then_sorted(seeded):
    """9618_s22_42:2(b)(ii) MP2-MP3 and 9618_s22_42:2(b)(iii) MP1: grid output before and after the sort."""
    before, after, _ = grids(seeded)
    assert before != after, "the same grid was output twice (call the procedure before AND after sorting)"
    assert _sorted_on_one_dimension(before, after)


# ---------------------------------------------------------------- 2(c)(i)

def array_with_first_row(row):
    return [list(row)] + [[100 - j for j in range(10)] for _ in range(9)]


@pytest.mark.parametrize("value,index", [(7, 1), (10, 2), (28, 4), (61, 7), (62, 8)])
def test_2c_i_finds_value_in_first_row(sol, value, index):
    """9618_s22_42:2(c)(i) MP1, MP3: completed statements return the index where the value is found."""
    assert sol.BinarySearch(array_with_first_row(ROW), 0, 9, value) == index


@pytest.mark.parametrize("value", [0, 1])
def test_2c_i_not_found_returns_minus_1(sol, value):
    """9618_s22_42:2(c)(i) MP1: RETURN -1 when the value is not in the first row."""
    assert sol.BinarySearch(array_with_first_row(ROW), 0, 9, value) == -1


def test_2c_i_is_recursive(sol, monkeypatch):
    """9618_s22_42:2(c)(i) MP2: the function calls itself (recursive calls with Lower / Upper)."""
    original = sol.BinarySearch
    calls = []

    def counting(*args):
        calls.append(args[1:3])
        return original(*args)

    monkeypatch.setattr(sol, "BinarySearch", counting)
    assert counting(array_with_first_row(ROW), 0, 9, 7) == 1
    assert len(calls) >= 2, "BinarySearch did not call itself"
    assert calls[1] == (0, 3), f"second call should search Lower=0 .. Mid-1=3, got {calls[1]}"


# ---------------------------------------------------------------- 2(c)(ii)

def test_2c_ii_screenshot_index_and_minus_1(seeded):
    """9618_s22_42:2(c)(ii) MP1-MP2: one returned index (found) and -1 (not found) output after the grids."""
    _, _, tail = grids(seeded)
    values = [int(v) for ln in tail for v in re.findall(r"-?\d+", ln)]
    assert -1 in values, "no -1 output for the number that is not in the first line"
    assert any(0 <= v <= 9 for v in values), "no index 0..9 output for the number that is found"
