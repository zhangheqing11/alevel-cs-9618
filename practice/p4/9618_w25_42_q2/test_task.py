"""Tests for 9618_w25_42 Question 2 (20 unique random integers, bubble sort, recursive binary search).

Mark point numbers are corpus markpoints[].n (they match the MS bullets here).
The main program uses random numbers, so script tests run it through a small
wrapper that seeds `random` first; the same seed gives the same array, which lets
a first run discover the array and later runs search for its smallest / largest value.
"""
import random
import re

import pytest

from testkit import output_lines, run_script

SEEDS = [1, 2, 3, 4, 5, 6, 7, 8]
NOT_IN_ARRAY = 999  # outside 0-100, so never in the array


def ints(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]


def run_seeded(candidate_path, tmp_path, seed, stdin):
    wrapper = tmp_path / f"seeded_{seed}.py"
    wrapper.write_text(
        "import random, runpy, sys\n"
        f"random.seed({seed})\n"
        f"sys.argv = [{str(candidate_path)!r}]\n"
        f"runpy.run_path({str(candidate_path)!r}, run_name='__main__')\n",
        encoding="utf-8",
    )
    return run_script(wrapper, stdin=stdin)


def arrays_in(stdout):
    """Output lines holding exactly 20 integers (the PrintArray lines), in order."""
    return [ints(line) for line in output_lines(stdout) if len(ints(line)) == 20]


class NoSortList(list):
    def sort(self, *args, **kwargs):
        raise AssertionError("do not use an inbuilt sorting method (QP 2(c))")


def no_sorted(*args, **kwargs):
    raise AssertionError("do not use an inbuilt sorting method (QP 2(c))")


def count_calls(monkeypatch, sol, name):
    original = getattr(sol, name)
    calls = []

    def spy(*args):
        calls.append(args)
        return original(*args)

    monkeypatch.setattr(sol, name, spy)
    return spy, calls


# ---------------------------------------------------------------- 2(a), 2(d)

def test_2a_twenty_unique_random_integers_0_to_100(candidate_path, tmp_path):
    """9618_w25_42:2(a) MP1-MP3: 20 integers between 0 and 100 inclusive, all different, generated at random."""
    first_arrays = []
    for seed in SEEDS:
        result = run_seeded(candidate_path, tmp_path, seed, f"{NOT_IN_ARRAY}\n")
        assert result.returncode == 0, result.stderr
        arrays = arrays_in(result.stdout)
        assert arrays, "no line with the 20 integers was output"
        values = arrays[0]
        assert all(0 <= v <= 100 for v in values), f"values outside 0-100: {values}"
        assert len(set(values)) == 20, f"the 20 integers are not unique: {values}"
        first_arrays.append(values)
    assert len({tuple(a) for a in first_arrays}) > 1, "the array is the same every run: not random"


def test_2d_screenshot_unsorted_sorted_line_then_sorted(candidate_path, tmp_path):
    """9618_w25_42:2(d)(ii) MP-03 (and 2(d)(i) MP1-MP3): unsorted array, "Sorted", the same integers ascending."""
    result = run_seeded(candidate_path, tmp_path, 1, f"{NOT_IN_ARRAY}\n")
    assert result.returncode == 0, result.stderr
    lines = output_lines(result.stdout)
    arrays = arrays_in(result.stdout)
    assert len(arrays) >= 2, "expected the array output twice (before and after sorting)"
    before, after = arrays[0], arrays[1]
    assert after == sorted(before)
    sorted_at = next(i for i, line in enumerate(lines) if "Sorted" in line)
    assert any(ints(line) == before for line in lines[:sorted_at])
    assert any(ints(line) == after for line in lines[sorted_at:])


# ---------------------------------------------------------------- 2(b)

def test_2b_printarray_single_line_with_spaces(sol, capsys):
    """9618_w25_42:2(b) MP1-MP3: the array output once, on one line, a space between each integer."""
    data = list(range(100, 0, -5))  # 20 integers
    sol.PrintArray(data)
    assert " ".join(str(v) for v in data) in output_lines(capsys.readouterr().out)


# ---------------------------------------------------------------- 2(c)

@pytest.mark.parametrize("data", [
    [57, 3, 88, 12, 0, 100, 41, 26, 75, 9, 64, 32, 18, 99, 50, 7, 83, 21, 46, 70],
    list(range(30, 0, -1)),
    [5, 1],
    [42],
    [],
])
def test_2c_bubblesort_any_length(sol, data):
    """9618_w25_42:2(c) MP1-MP5: returns the array sorted ascending, for arrays of any length."""
    assert list(sol.BubbleSort(list(data))) == sorted(data)


def test_2c_no_inbuilt_sort(sol, monkeypatch):
    """9618_w25_42:2(c) MP2-MP4: QP forbids an inbuilt sorting method (no list.sort(), no sorted())."""
    monkeypatch.setattr(sol, "sorted", no_sorted, raising=False)
    data = NoSortList([9, 4, 7, 1, 8, 2])
    assert list(sol.BubbleSort(data)) == [1, 2, 4, 7, 8, 9]


# ---------------------------------------------------------------- 2(e)

SORTED20 = [2, 5, 9, 14, 17, 23, 30, 31, 38, 44, 51, 56, 62, 67, 73, 79, 85, 90, 96, 100]


def test_2e_finds_every_index(sol):
    """9618_w25_42:2(e) MP2-MP5: every value in the sorted array is found at its index."""
    for index, value in enumerate(SORTED20):
        assert sol.RecursiveBinarySearch(SORTED20, 0, 19, value) == index


@pytest.mark.parametrize("missing", [0, 1, 3, 50, 99, 101])
def test_2e_returns_minus_one_when_not_found(sol, missing):
    """9618_w25_42:2(e) MP6: -1 when the value is not in the array (below, inside and above the range)."""
    assert sol.RecursiveBinarySearch(SORTED20, 0, 19, missing) == -1


def test_2e_is_recursive_and_halves(sol, monkeypatch):
    """9618_w25_42:2(e) MP1-MP2, MP4-MP5: recursive calls, each halving the range (at most 6 calls for 20 items)."""
    spy, calls = count_calls(monkeypatch, sol, "RecursiveBinarySearch")
    assert spy(SORTED20, 0, 19, 2) == 0
    assert 1 < len(calls) <= 6, f"{len(calls)} calls: expected a recursive binary search"
    calls.clear()
    assert spy(SORTED20, 0, 19, 100) == 19
    assert 1 < len(calls) <= 6


# ---------------------------------------------------------------- 2(f)

def test_2f_screenshot_smallest_largest_missing(candidate_path, tmp_path):
    """9618_w25_42:2(f)(ii) MP1-MP2 (and 2(f)(i) MP1-MP3): smallest -> found at 0, largest -> found at 19, missing -> Not found."""
    probe = run_seeded(candidate_path, tmp_path, 3, f"{NOT_IN_ARRAY}\n")
    assert probe.returncode == 0, probe.stderr
    assert "Not found" in probe.stdout
    assert "Found at position" not in probe.stdout
    values = arrays_in(probe.stdout)[0]
    for value, index in [(min(values), 0), (max(values), 19)]:
        result = run_seeded(candidate_path, tmp_path, 3, f"{value}\n")
        assert result.returncode == 0, result.stderr
        found = re.search(r"Found at position\s+(\d+)", result.stdout)
        assert found, f"no found message and position for {value}"
        assert int(found.group(1)) == index, f"{value} should be found at position {index}"


def test_2di_2fi_traced_main(candidate_path):
    """9618_w25_42:2(d)(i) MP1–3; 2(f)(i) MP2–3; MS pp.22,25."""
    from testkit import run_script_traced
    state = random.getstate()
    try:
        random.seed(3)
        r = run_script_traced(candidate_path, stdin="999\n")
    finally:
        random.setstate(state)
    assert r.error is None
    prints, sorts, searches = r.called("PrintArray"), r.called("BubbleSort"), r.called("RecursiveBinarySearch")
    assert len(prints) >= 2 and sorts and searches
    before = list(prints[0].args.values())[0]
    assert list(sorts[0].args.values())[0] == before
    assert sorts[0].result == sorted(before)
    assert list(prints[-1].args.values())[0] == sorts[0].result
    search = searches[0]
    # QP specifies the four argument roles; parameter names may vary.
    assert list(search.args.values()) == [sorts[0].result, 0, 19, 999]
    assert search.result == -1 and "Not found" in r.stdout
    assert next(i for i, c in enumerate(r.calls) if c is prints[0]) < next(i for i, c in enumerate(r.calls) if c is sorts[0]) < next(i for i, c in enumerate(r.calls) if c is prints[-1]) < next(i for i, c in enumerate(r.calls) if c is search)
