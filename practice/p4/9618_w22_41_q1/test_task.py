"""Tests for 9618_w22_41 Question 1 (IntegerData.txt: read, count, bubble sort).

Mark point numbers are corpus markpoints[].n (they match the MS bullets here).
"""
import builtins
import io
import re

import pytest

from testkit import run_script, use_files

DATA_FILE = "IntegerData.txt"


def official_data(exercise_dir):
    return [int(x) for x in (exercise_dir / "files" / DATA_FILE).read_text().split()]


def feed(monkeypatch, *answers):
    """Replace input(); fail if the program asks for more input than given.
    Returns the list of answers still unused (empty = all consumed)."""
    queue = list(answers)

    def fake_input(prompt=""):
        if not queue:
            raise AssertionError("program asked for more input than the test provides")
        return queue.pop(0)

    monkeypatch.setattr(builtins, "input", fake_input)
    return queue


def watch_open(monkeypatch):
    """Keep every opened handle so a missing close() cannot be hidden by GC."""
    real_open = builtins.open
    handles = []

    def tracked(*args, **kwargs):
        handle = real_open(*args, **kwargs)
        handles.append(handle)
        return handle

    monkeypatch.setattr(builtins, "open", tracked)
    monkeypatch.setattr(io, "open", tracked)
    return handles


def ints(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]


def contains_run(values, wanted):
    return any(values[i:i + len(wanted)] == wanted for i in range(len(values) - len(wanted) + 1))


def message_numbers(stdout):
    """Integers on output lines that contain words (the message line, which also
    carries the input() prompt because input() does not end the line, D13)."""
    assert re.search(r"[A-Za-z]", stdout), "the count needs an appropriate message"
    return ints(stdout)


# ---------------------------------------------------------------- 1(a)

def test_1a_dataarray_has_100_elements(sol):
    """9618_w22_41:1(a) MP1-MP2: global 1D array DataArray with 100 elements (D10 ①)."""
    assert isinstance(sol.DataArray, list), "DataArray must be a real list (array), not just a comment"
    assert len(sol.DataArray) == 100


# ---------------------------------------------------------------- 1(b)

def test_1b_readfile_stores_all_100_integers(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w22_41:1(b) MP2-MP4: opens IntegerData.txt, loops 100 / to EOF, stores every value as an integer."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    sol.ReadFile()
    assert sol.DataArray == official_data(exercise_dir)


def test_1b_readfile_closes_file(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w22_41:1(b) MP5: the file is closed."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    handles = watch_open(monkeypatch)
    sol.ReadFile()
    assert handles, "ReadFile() did not open a file"
    assert all(h.closed for h in handles), "IntegerData.txt is left open"


def test_1b_missing_file_is_handled(sol, monkeypatch, tmp_path, capsys):
    """9618_w22_41:1(b) MP6-MP7: exception handling with an output message when the file is missing."""
    monkeypatch.chdir(tmp_path)  # empty folder: no IntegerData.txt
    sol.ReadFile()
    assert capsys.readouterr().out.strip(), "no message was output for the missing file"


# ---------------------------------------------------------------- 1(c)

def test_1c_rejects_out_of_range_then_counts(sol, monkeypatch, exercise_dir):
    """9618_w22_41:1(c) MP1-MP3, MP5-MP7: 0 and 101 are rejected, 61 is accepted and found twice."""
    sol.DataArray = official_data(exercise_dir)
    left = feed(monkeypatch, "0", "101", "61")
    assert sol.FindValues() == 2
    assert left == [], "FindValues() stopped asking before a valid number was entered"


def test_1c_accepts_both_bounds(sol, monkeypatch):
    """9618_w22_41:1(c) MP3: 1 and 100 are valid (inclusive)."""
    sol.DataArray = [1] * 3 + [100] * 5 + [50] * 92
    feed(monkeypatch, "1")
    assert sol.FindValues() == 3
    feed(monkeypatch, "100")
    assert sol.FindValues() == 5


def test_1c_checks_all_100_elements(sol, monkeypatch, exercise_dir):
    """9618_w22_41:1(c) MP4: the loop reaches the last element (19 is only at index 99 of IntegerData.txt)."""
    sol.DataArray = official_data(exercise_dir)
    feed(monkeypatch, "19")
    assert sol.FindValues() == 1


def test_1c_returns_zero_when_absent(sol, monkeypatch, exercise_dir):
    """9618_w22_41:1(c) MP6-MP7: counter starts at 0 and is returned (1 is not in the file)."""
    sol.DataArray = official_data(exercise_dir)
    feed(monkeypatch, "1")
    assert sol.FindValues() == 0


# ---------------------------------------------------------------- 1(d)

def test_1d_screenshot_input_61_outputs_2(candidate_path, exercise_dir):
    """9618_w22_41:1(d)(ii) MP-03: input 61 -> output 2 (also checks 1(d)(i) MP1-MP3 end to end)."""
    result = run_script(candidate_path, stdin="61\n", files_dir=exercise_dir / "files")
    assert result.returncode == 0, result.stderr
    assert 2 in message_numbers(result.stdout), "the count 2 is not output with a message"


def test_1d_main_revalidates_and_outputs_count(candidate_path, exercise_dir):
    """9618_w22_41:1(d)(i) MP1-MP3: ReadFile() then FindValues(); 101 rejected, 8 found 3 times and output."""
    result = run_script(candidate_path, stdin="101\n8\n", files_dir=exercise_dir / "files")
    assert result.returncode == 0, "program asked for more input than given, or crashed:\n" + result.stderr
    assert 3 in message_numbers(result.stdout)


# ---------------------------------------------------------------- 1(e)

def test_1e_bubblesort_sorts_and_prints_official_data(sol, capsys, exercise_dir):
    """9618_w22_41:1(e) MP1-MP4: sorts DataArray ascending and outputs the sorted contents."""
    data = official_data(exercise_dir)
    sol.DataArray = list(data)
    sol.BubbleSort()
    assert sol.DataArray == sorted(data)
    assert contains_run(ints(capsys.readouterr().out), sorted(data)), "sorted array is not output by BubbleSort()"


def test_1e_bubblesort_reverse_order(sol, capsys):
    """9618_w22_41:1(e) MP2-MP4: worst case (reverse order) is fully sorted."""
    sol.DataArray = list(range(100, 0, -1))
    sol.BubbleSort()
    assert sol.DataArray == list(range(1, 101))


def test_1e_main_calls_bubblesort(candidate_path, exercise_dir):
    """9618_w22_41:1(e) MP1: BubbleSort() is called from the main program (sorted data is the last output)."""
    result = run_script(candidate_path, stdin="61\n", files_dir=exercise_dir / "files")
    assert result.returncode == 0, result.stderr
    assert contains_run(ints(result.stdout), sorted(official_data(exercise_dir)))


def test_1di_1e_traced_main(candidate_path, exercise_dir):
    """9618_w22_41:1(d)(i) MP1–3; 1(e) MP1; MS pp.6–7."""
    from testkit import run_script_traced
    for value, expected in ((61, 2), (8, 3)):
        r = run_script_traced(candidate_path, stdin=f"{value}\n", files_dir=exercise_dir / "files")
        assert r.error is None
        read, find, sort = r.called("ReadFile"), r.called("FindValues"), r.called("BubbleSort")
        assert read and find and sort
        assert next(i for i, c in enumerate(r.calls) if c is read[0]) < next(i for i, c in enumerate(r.calls) if c is find[0]) < next(i for i, c in enumerate(r.calls) if c is sort[0])
        assert find[0].result == expected and expected in ints(r.stdout)
