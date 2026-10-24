"""Tests for 9618_w25_43 Question 3 (recursive count in an array; split a string without split()).

Mark point numbers are corpus markpoints[].n (they match the MS bullets here).
RecursiveCount() is always called with keyword arguments named as in the QP
(ArrayCopy, NumberElements, DataToFind), so either parameter order is accepted.
"""
import copy
import inspect
import re
import runpy
import sys

import pytest

from testkit import run_script

GIVEN = [0, 5, 1, 2, 5, 9, 9, 6, 5, 0]  # QP 3(a)(ii), in order
CODE = "x=0;y=1;x=x+y;y++;"  # QP 3(b)
SPLIT = ["x=0", "y=1", "x=x+y", "y++"]


def ints(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]


def count(sol, array, number, find):
    return sol.RecursiveCount(ArrayCopy=list(array), NumberElements=number, DataToFind=find)


def spy_on_recursivecount(monkeypatch, sol):
    """Record every call (recursive ones go through the module global) as {parameter: value}."""
    original = sol.RecursiveCount
    signature = inspect.signature(original)
    calls = []

    def spy(*args, **kwargs):
        bound = signature.bind(*args, **kwargs)
        calls.append({k: copy.deepcopy(v) for k, v in bound.arguments.items()})
        return original(*args, **kwargs)

    monkeypatch.setattr(sol, "RecursiveCount", spy)
    return spy, calls


def trace_main(path, subroutines=("RecursiveCount", "SplitData")):
    """Run the program as __main__ in-process. Returns (values, first_calls):
    every list / str value held by a main-program variable, and the arguments of the
    first call to each subroutine."""
    filename = str(path)
    values, first_calls = [], {}

    def local_tracer(frame, event, arg):
        for value in list(frame.f_locals.values()):
            if isinstance(value, (list, str)) and value not in values:
                values.append(copy.deepcopy(value))
        return local_tracer

    def global_tracer(frame, event, arg):
        if frame.f_code.co_filename != filename:
            return None
        name = frame.f_code.co_name
        if name in subroutines:
            first_calls.setdefault(name, copy.deepcopy(dict(frame.f_locals)))
            return None
        return local_tracer

    sys.settrace(global_tracer)
    try:
        runpy.run_path(filename, run_name="__main__")
    finally:
        sys.settrace(None)
    return values, first_calls


class NoSplitStr(str):
    """A str whose split-style methods raise; indexing and iteration give plain characters."""

    def _forbidden(self, *args, **kwargs):
        raise AssertionError("do not use an inbuilt function to split the string (QP 3(b)(ii))")

    split = rsplit = partition = rpartition = splitlines = _forbidden


# ---------------------------------------------------------------- 3(a)

@pytest.mark.parametrize("array, find, expected", [
    (GIVEN, 0, 2),
    (GIVEN, 5, 3),
    (GIVEN, 9, 2),
    (GIVEN, 7, 0),
    ([4, 4, 4, 4], 4, 4),
    ([], 3, 0),
])
def test_3ai_recursivecount_counts(sol, array, find, expected):
    """9618_w25_43:3(a)(i) MP2-MP5: 0 for no elements; first element compared; +1 on a match."""
    assert count(sol, array, len(array), find) == expected


def test_3ai_each_call_drops_the_first_element(sol, monkeypatch):
    """9618_w25_43:3(a)(i) MP4-MP6: recursive; every call gets the array without its first element,
    NumberElements - 1 and the same DataToFind, down to 0 elements."""
    spy, calls = spy_on_recursivecount(monkeypatch, sol)
    assert spy(ArrayCopy=list(GIVEN), NumberElements=10, DataToFind=0) == 2
    assert len(calls) == 11, f"expected 11 calls (10 elements + the base case), got {len(calls)}"
    for k, call in enumerate(calls):
        assert list(call["ArrayCopy"]) == GIVEN[k:]
        assert call["NumberElements"] == 10 - k
        assert call["DataToFind"] == 0


def test_3aii_main_stores_array_and_passes_parameters(candidate_path, monkeypatch, tmp_path, capsys):
    """9618_w25_43:3(a)(ii) MP1-MP2: the 10 given integers in order in an array; RecursiveCount(0, array, 10)."""
    monkeypatch.chdir(tmp_path)
    values, first_calls = trace_main(candidate_path)
    capsys.readouterr()
    assert GIVEN in values, "the array 0 5 1 2 5 9 9 6 5 0 is not stored in the main program"
    call = first_calls.get("RecursiveCount")
    assert call is not None, "RecursiveCount() is not called from the main program"
    assert list(call["ArrayCopy"]) == GIVEN and call["NumberElements"] == 10 and call["DataToFind"] == 0


def test_3aiii_screenshot_outputs_2(candidate_path):
    """9618_w25_43:3(a)(iii) MP-03 (and 3(a)(ii) MP3): the return value 2 is output (before the split lines)."""
    result = run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    lines = [line.strip() for line in result.lines]
    assert 2 in [n for line in lines for n in ints(line)]


# ---------------------------------------------------------------- 3(b)

def test_3bi_main_stores_the_string(candidate_path, monkeypatch, tmp_path, capsys):
    """9618_w25_43:3(b)(i) MP: the string "x=0;y=1;x=x+y;y++;" is stored in a main-program variable."""
    monkeypatch.chdir(tmp_path)
    values, first_calls = trace_main(candidate_path)
    capsys.readouterr()
    assert CODE in values, 'the string "x=0;y=1;x=x+y;y++;" is not stored in a variable in the main program'


@pytest.mark.parametrize("text, expected", [
    (CODE, SPLIT),
    ("a=1;b=2;c=a*b;print(c);", ["a=1", "b=2", "c=a*b", "print(c)"]),
    ("n=10;m=n-1;n=m;m--;", ["n=10", "m=n-1", "n=m", "m--"]),
])
def test_3bii_splitdata_four_statements(sol, text, expected):
    """9618_w25_43:3(b)(ii) MP2-MP6: four statements, each in its own element, without the semi-colons."""
    result = list(sol.SplitData(text))
    assert result[:4] == expected
    assert all(item in ("", None) for item in result[4:]), "extra array elements must be unused"


def test_3bii_no_inbuilt_split(sol):
    """9618_w25_43:3(b)(ii) MP2-MP4: QP forbids an inbuilt split function; characters are compared to ';'."""
    assert list(sol.SplitData(NoSplitStr(CODE)))[:4] == SPLIT


def test_3biii_main_calls_splitdata_with_the_string(candidate_path, monkeypatch, tmp_path, capsys):
    """9618_w25_43:3(b)(iii) MP1: SplitData() is called with the string from 3(b)(i)."""
    monkeypatch.chdir(tmp_path)
    values, first_calls = trace_main(candidate_path)
    capsys.readouterr()
    call = first_calls.get("SplitData")
    assert call is not None, "SplitData() is not called from the main program"
    assert CODE in call.values()


def test_3biv_screenshot_four_lines(candidate_path):
    """9618_w25_43:3(b)(iv) MP-03 (and 3(b)(iii) MP1-MP2): x=0 / y=1 / x=x+y / y++ on separate lines."""
    result = run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    lines = [line.strip() for line in result.lines]
    remaining = iter(lines)
    for expected in SPLIT:
        assert any(expected in line for line in remaining), f"missing separate output line: {expected}"


def test_3aii_3biii_traced_results(candidate_path):
    """9618_w25_43:3(a)(ii) MP2–3; 3(b)(iii) MP1–2; MS pp.34,38."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path)
    assert r.error is None
    counts, splits = r.called("RecursiveCount"), r.called("SplitData")
    assert counts and splits
    assert counts[0].args == {"ArrayCopy": GIVEN, "NumberElements": 10, "DataToFind": 0}
    assert counts[0].result == 2
    assert CODE in splits[0].args.values() and list(splits[0].result)[:4] == SPLIT
    assert next(i for i, c in enumerate(r.calls) if c is counts[0]) < next(i for i, c in enumerate(r.calls) if c is splits[0])
    assert counts[0].result in ints(r.stdout)
    remaining = iter(r.stdout.splitlines())
    assert all(any(item in line for line in remaining) for item in splits[0].result[:4])
