"""9618_s24_41 Question 1 (DataStored, Initialise, BubbleSort, BinarySearch): tests from the exact matching MS.

Function tests set the globals DataStored / NumberItems themselves. Unused slots are padded with
999 (bigger than every test value), so the tests work whether a program sorts / searches only the
first NumberItems slots or the whole 20-element array (the MS accepts both: 'found in index 16').
Screenshot cells run the whole program; values are read as the stream of integers in the output
with zeros dropped (unused slots of a printed 20-element array).
"""
import re

import pytest

from testkit import feed_input, run_script

PAD = 999


def set_data(sol, values):
    sol.DataStored = list(values) + [PAD] * (20 - len(values))
    sol.NumberItems = len(values)


def int_stream(text):
    return [int(v) for v in re.findall(r"-?\d+", text) if int(v) != 0]


def contains_run(stream, run):
    return any(stream[i:i + len(run)] == run for i in range(len(stream) - len(run) + 1))


def run(candidate_path, *values):
    return run_script(candidate_path, stdin="".join(f"{v}\n" for v in values))


# ---------------------------------------------------------------- 1(a)

def test_1a_globals_declared(sol):
    """9618_s24_41:1(a) MP1: global array DataStored (20 integers) and global NumberItems."""
    assert isinstance(getattr(sol, "DataStored", None), list), "no global list called DataStored"
    assert len(sol.DataStored) == 20, "DataStored must have space for 20 integers (D10: build the real list)"
    assert hasattr(sol, "NumberItems"), "no global variable NumberItems"


# ---------------------------------------------------------------- 1(b)

def test_1b_initialise_rejects_30_then_stores_five(sol, monkeypatch):
    """9618_s24_41:1(b) MP2-MP5: quantity 30 rejected, 5 accepted, five integers stored in order."""
    sol.DataStored = [0] * 20
    sol.NumberItems = 0
    feed_input(monkeypatch, "30", "5", "3", "9", "4", "1", "2")
    sol.Initialise()
    assert sol.NumberItems == 5
    assert sol.DataStored[:5] == [3, 9, 4, 1, 2]


@pytest.mark.parametrize("answers,expected", [
    (("0", "21", "1", "7"), [7]),
    (("20",) + tuple(str(n) for n in range(1, 21)), list(range(1, 21))),
])
def test_1b_initialise_quantity_1_to_20_inclusive(sol, monkeypatch, answers, expected):
    """9618_s24_41:1(b) MP3: 0 and 21 rejected; 1 and 20 accepted."""
    sol.DataStored = [0] * 20
    sol.NumberItems = 0
    feed_input(monkeypatch, *answers)
    sol.Initialise()
    assert sol.NumberItems == len(expected)
    assert sol.DataStored[:len(expected)] == expected


# ---------------------------------------------------------------- 1(c)

def test_1c_ii_screenshot_invalid_30_then_array(candidate_path):
    """9618_s24_41:1(c)(i) MP1-MP2 and 9618_s24_41:1(c)(ii) MP1-MP2: 30 rejected, 5 accepted, array output 3 9 4 1 2."""
    res = run(candidate_path, 30, 5, 3, 9, 4, 1, 2, 2)
    assert res.returncode == 0, "crashed or asked for more input than given (was 30 accepted?):\n" + res.stderr[-500:]
    assert contains_run(int_stream(res.stdout), [3, 9, 4, 1, 2]), "array output 3 9 4 1 2 not found"


# ---------------------------------------------------------------- 1(d)

@pytest.mark.parametrize("values", [[3, 9, 4, 1, 2], [5, 4, 3, 2, 1], [1, 2, 3], [7, 7, 1, 7], [42]])
def test_1d_i_bubble_sort_ascending(sol, values):
    """9618_s24_41:1(d)(i) MP1-MP4: outer and inner loop, comparison and swap give ascending order."""
    set_data(sol, values)
    sol.BubbleSort()
    assert sol.DataStored[:len(values)] == sorted(values)


def test_1d_iii_screenshot_sorted(candidate_path):
    """9618_s24_41:1(d)(ii) MP1 and 9618_s24_41:1(d)(iii) MP1: after BubbleSort the values are output as 1 2 3 4 9."""
    res = run(candidate_path, 5, 3, 9, 4, 1, 2, 2)
    assert res.returncode == 0, res.stderr[-500:]
    stream = int_stream(res.stdout)
    assert contains_run(stream, [3, 9, 4, 1, 2]) and contains_run(stream, [1, 2, 3, 4, 9]), \
        "expected the array output before (3 9 4 1 2) and after sorting (1 2 3 4 9)"


# ---------------------------------------------------------------- 1(e)

@pytest.mark.parametrize("value,index", [(1, 0), (2, 1), (6, 2), (8, 3), (10, 4)])
def test_1e_i_binary_search_found(sol, value, index):
    """9618_s24_41:1(e)(i) MP2-MP5: mid value, compare, move Last / First, return the index."""
    set_data(sol, [1, 2, 6, 8, 10])
    assert sol.BinarySearch(value) == index


@pytest.mark.parametrize("value", [7, 0, 11])
def test_1e_i_binary_search_not_found(sol, value):
    """9618_s24_41:1(e)(i) MP6: loop ends and -1 is returned when the value is not there."""
    set_data(sol, [1, 2, 6, 8, 10])
    assert sol.BinarySearch(value) == -1


def test_1e_i_binary_search_larger_array(sol):
    """9618_s24_41:1(e)(i) MP2-MP6: works for every position of a full 20-element array."""
    values = list(range(5, 105, 5))
    sol.DataStored = list(values)
    sol.NumberItems = 20
    for i, v in enumerate(values):
        assert sol.BinarySearch(v) == i
    assert sol.BinarySearch(52) == -1


def test_1e_iii_screenshot_test_1_found(candidate_path):
    """9618_s24_41:1(e)(ii) MP1-MP3 and 9618_s24_41:1(e)(iii) MP1 (test 1): 2 is found at index 1 (MS accepts 16)."""
    res = run(candidate_path, 5, 1, 6, 2, 8, 10, 2)
    assert res.returncode == 0, res.stderr[-500:]
    last = re.findall(r"-?\d+", res.stdout)[-1]
    assert int(last) in (1, 16), f"last value output should be the index of 2, got {last}"


def test_1e_iii_screenshot_test_2_not_found(candidate_path):
    """9618_s24_41:1(e)(iii) MP1 (test 2): 7 is not found, -1 output."""
    res = run(candidate_path, 5, 1, 6, 2, 8, 10, 7)
    assert res.returncode == 0, res.stderr[-500:]
    assert re.findall(r"-?\d+", res.stdout)[-1] == "-1"
