"""s25/43 Q2: exact QP pp.4–6 and MS pp.19–32."""
import ast
import re
import runpy
import sys

import pytest
from testkit import run_script

ORIGINAL = [0, 3, 4, 56, 67, 44, 43, 32, 31, 345, 45, 6, 54, 1]


def ints(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]


def test_2a_di_fi_main_call_sequence(candidate_path):
    """9618_s25_43:2(a) whole; 2(d)(i) MP1–MP2; 2(f)(i) MP1: initialise, output/sort/output, four searches."""
    calls = []
    def profile(frame, event, arg):
        if event != "call" or frame.f_code.co_filename != str(candidate_path):
            return
        name = frame.f_code.co_name
        if name not in ("OutputArray", "InsertionSort", "Search"):
            return
        # Do not count a recursive search's internal calls as main calls.
        if frame.f_back.f_code.co_name == name:
            return
        values = list(frame.f_locals.values())
        calls.append((name, [list(v) if isinstance(v, list) else v for v in values]))
    old = sys.getprofile()
    try:
        sys.setprofile(profile)
        runpy.run_path(str(candidate_path), run_name="__main__")
    finally:
        sys.setprofile(old)
    assert [name for name, _ in calls] == ["OutputArray", "InsertionSort", "OutputArray", "Search", "Search", "Search", "Search"]
    assert calls[0][1][0] == ORIGINAL
    assert calls[1][1][0] == ORIGINAL
    assert calls[2][1][0] == sorted(ORIGINAL)
    assert [args[1] for name, args in calls if name == "Search"] == [0, 345, 67, 2]
    assert all(args[0] == sorted(ORIGINAL) for name, args in calls if name == "Search")


@pytest.mark.parametrize("values", [ORIGINAL, [], [3], [5, 4, 3, 2, 1], [3, 1, 3, 0, 1], [1, 2, 3]])
def test_2b_insertion_sort(sol, values):
    """9618_s25_43:2(b) MP1–MP5: return ascending array, shift and insert, no values lost."""
    assert sol.InsertionSort(list(values)) == sorted(values)


@pytest.mark.parametrize("values", [ORIGINAL, [8, 0, -2, 8], [4]])
def test_2c_output_format(sol, capsys, values):
    """9618_s25_43:2(c) MP1–MP2: every item in order, one line with spaces."""
    sol.OutputArray(list(values))
    lines = capsys.readouterr().out.strip().splitlines()
    assert any(line.split() == [str(x) for x in values] for line in lines)


def test_2dii_screenshot_unsorted_then_sorted(candidate_path):
    """9618_s25_43:2(d)(ii) whole: MS p.25 unsorted then sorted integer rows."""
    res = run_script(candidate_path)
    assert res.returncode == 0, res.stderr
    lines = [ints(line) for line in res.lines]
    a = next(i for i, values in enumerate(lines) if values == ORIGINAL)
    assert any(values == sorted(ORIGINAL) for values in lines[a + 1:])


@pytest.mark.parametrize("value,index", [(0, 0), (345, 13), (67, 12), (2, -1), (-1, -1), (346, -1), (32, 6)])
def test_2e_search_found_and_missing(sol, value, index):
    """9618_s25_43:2(e) MP2–MP6: both bounds, middle equality and -1 if absent."""
    assert sol.Search(sorted(ORIGINAL), value) == index
    assert sol.Search([], value) == -1
    assert sol.Search([value], value) == 0


def test_2e_search_halves_interval(sol):
    """9618_s25_43:2(e) MP3–MP6: binary interval narrowing rather than a linear scan."""
    class ObservedList(list):
        def __init__(self, values):
            super().__init__(values)
            self.reads = 0
        def __getitem__(self, index):
            self.reads += 1
            return super().__getitem__(index)
        def __iter__(self):
            # Make an iteration-based linear search visible too.
            for index in range(len(self)):
                yield self[index]
    for value, expected in [(0, 0), (512, 256), (511, -1)]:
        values = ObservedList(range(0, 514, 2))
        assert sol.Search(values, value) == expected
        assert values.reads <= 36, "binary search should inspect only successive middle positions"


def test_2fii_screenshot_locations(candidate_path):
    """9618_s25_43:2(f)(i) MP2; 2(f)(ii) whole: MS p.32 locations 0,13,12 then not found."""
    res = run_script(candidate_path)
    assert res.returncode == 0, res.stderr
    lines = res.lines
    # Locate the sorted row, then inspect each of the four search results.
    sorted_row = next(i for i, line in enumerate(lines) if ints(line) == sorted(ORIGINAL))
    results = lines[sorted_row + 1:]
    position = 0
    for index in [0, 13, 12]:
        while position < len(results) and (not ints(results[position]) or ints(results[position])[-1] != index):
            position += 1
        assert position < len(results), f"missing index {index} in search output"
        position += 1
    failure_message = " ".join(results[position:])
    assert any(char.isalpha() for char in failure_message), "not-found outcome needs an appropriate message"



def test_2b_e_no_builtin_shortcuts(candidate_path):
    """9618_s25_43:2(b) MP2–MP5 and 2(e) MP3–MP6; D10 forbids builtin sorting/searching."""
    tree = ast.parse(candidate_path.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, "attr", "")
            assert name not in {"sort", "sorted", "index", "count", "max", "min", "bisect_left", "bisect_right", "insort"}
        if isinstance(node, ast.Compare):
            assert not any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops)


def test_2di_2fi_traced_results(candidate_path):
    """9618_s25_43:2(d)(i) MP1–2; 2(f)(i) MP1–2; MS pp.24,31."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path)
    assert r.error is None
    sort, outputs, searches = r.called("InsertionSort"), r.called("OutputArray"), r.called("Search")
    assert sort and len(outputs) >= 2 and searches
    assert sort[0].args["DataArray"] == ORIGINAL
    assert sort[0].result == sorted(ORIGINAL)
    assert outputs[-1].args["DataArray"] == sort[0].result
    for value, expected in ((0, 0), (345, 13), (67, 12), (2, -1)):
        matches = [c for c in searches if c.args["ItemToFind"] == value and c.args["DataArray"] == sort[0].result]
        assert matches and matches[0].result == expected
    assert all(value in ints(r.stdout) for value in (0, 13, 12))
