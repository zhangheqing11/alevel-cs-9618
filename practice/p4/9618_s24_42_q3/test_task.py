"""Exact matching MS: s24/42 Q3, pp.28–39; D31 corrections in task.md."""
import ast
import inspect
import re
import runpy
import sys

import pytest
from testkit import run_script

ORIGINAL = [100, 85, 644, 22, 15, 8, 1]


def is_subsequence(wanted, seen):
    items = iter(seen)
    return all(any(value == item for item in items) for value in wanted)


def numbers(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]


def test_3a_bii_cii_main_calls_original_arrays(candidate_path):
    """9618_s24_42:3(a) whole; 3(b)(ii) MP1; 3(c)(ii) whole: both calls get original data."""
    calls = []
    declarations = []
    def profile(frame, event, arg):
        if event == "call" and frame.f_code.co_name in ("RecursiveInsertion", "IterativeInsertion"):
            # Record only calls made directly by the main program, not recursion.
            if frame.f_back.f_code.co_filename == str(candidate_path) and frame.f_back.f_code.co_name not in ("RecursiveInsertion", "IterativeInsertion"):
                arrays = [list(v) for v in frame.f_locals.values() if isinstance(v, list)]
                calls.append((frame.f_code.co_name, arrays))
                if "NumberArray" in frame.f_back.f_locals:
                    declarations.append(list(frame.f_back.f_locals["NumberArray"]))
    old = sys.getprofile()
    try:
        sys.setprofile(profile)
        runpy.run_path(str(candidate_path), run_name="__main__")
    finally:
        sys.setprofile(old)
    assert declarations and declarations[0] == ORIGINAL
    assert [name for name, _ in calls] == ["RecursiveInsertion", "IterativeInsertion"]
    assert all(ORIGINAL in arrays for _, arrays in calls)


@pytest.mark.parametrize("values", [[], [4], ORIGINAL, [4, 3, 2, 1], [2, 2, 1, 2], [1, 2, 3]])
def test_3bi_recursive_sort(sol, monkeypatch, values):
    """9618_s24_42:3(b)(i) MP1–MP3: recursive call, base case, shifts and loop control."""
    original = sol.RecursiveInsertion
    calls = []
    def counted(*args):
        calls.append(args[1])
        return original(*args)
    monkeypatch.setattr(sol, "RecursiveInsertion", counted)
    assert sol.RecursiveInsertion(list(values), len(values)) == sorted(values)
    if len(values) > 1:
        assert len(calls) > 1, "RecursiveInsertion must recurse"
    else:
        assert len(calls) == 1


@pytest.mark.parametrize("values", [[], [4], ORIGINAL, [4, 3, 2, 1], [2, 2, 1, 2], [1, 2, 3]])
def test_3ci_iterative_sort(sol, monkeypatch, values):
    """9618_s24_42:3(c)(i) MP1–MP4: return ascending array using iteration."""
    original = sol.IterativeInsertion
    calls = []
    def counted(*args):
        calls.append(1)
        return original(*args)
    def forbidden(*args):
        pytest.fail("IterativeInsertion must not delegate to RecursiveInsertion")
    monkeypatch.setattr(sol, "IterativeInsertion", counted)
    monkeypatch.setattr(sol, "RecursiveInsertion", forbidden)
    # MS permits an array parameter only; the second parameter is optional for this part.
    if len(inspect.signature(original).parameters) == 1:
        result = sol.IterativeInsertion(list(values))
    else:
        result = sol.IterativeInsertion(list(values), len(values))
    assert result == sorted(values)
    assert len(calls) == 1, "IterativeInsertion must not recurse"


def test_3biii_ciii_diii_screenshots(candidate_path):
    """9618_s24_42:3(b)(ii) MP2; 3(b)(iii), 3(c)(ii)/(iii), 3(d)(ii) MP1–2, 3(d)(iii) whole."""
    res = run_script(candidate_path)
    assert res.returncode == 0, res.stderr
    recursive, iterative = re.split(r"iterative", res.stdout, maxsplit=1, flags=re.I)
    assert re.search(r"recursive", recursive, re.I)
    assert is_subsequence([1, 8, 15, 22, 85, 100, 644], numbers(recursive))
    assert is_subsequence([1, 8, 15, 22, 85, 100, 644, 6], numbers(iterative))


@pytest.mark.parametrize("value", [1, 8, 15, 22, 85, 100, 644, 0, 10, 999])
def test_3di_recursive_binary_search(sol, monkeypatch, value):
    """9618_s24_42:3(d)(i) MP1–MP7: recursion, base case, middle and both half-intervals."""
    values = sorted(ORIGINAL)
    original = sol.BinarySearch
    calls = []
    def counted(*args):
        calls.append(args[1:3])
        return original(*args)
    monkeypatch.setattr(sol, "BinarySearch", counted)
    expected = values.index(value) if value in values else -1
    assert sol.BinarySearch(values, 0, len(values) - 1, value) == expected
    if value != 22:
        assert len(calls) > 1, "BinarySearch must recurse"
    assert sol.BinarySearch([], 0, -1, value) == -1


def test_3dii_main_not_found_branch(candidate_path, capsys):
    """9618_s24_42:3(d)(ii) MP2: failure result gives a message (wording checked manually)."""
    patched = []
    def profile(frame, event, arg):
        if event == "line" and frame.f_code.co_filename == str(candidate_path):
            if "BinarySearch" in frame.f_globals and not patched:
                # Inject a failure result to exercise the main program's selection;
                # the real search is independently checked above.
                frame.f_globals["BinarySearch"] = lambda *args: -1
                patched.append(True)
        return profile
    old = sys.gettrace()
    try:
        sys.settrace(profile)
        runpy.run_path(str(candidate_path), run_name="__main__")
    finally:
        sys.settrace(old)
    tail = re.split(r"iterative", capsys.readouterr().out, flags=re.I)[-1]
    assert patched
    # The last output must contain a message, rather than simply print -1.
    assert any(char.isalpha() for char in tail.strip().splitlines()[-1])


def test_3bi_ci_di_no_builtin_shortcuts(candidate_path):
    """9618_s24_42:3(b)(i) MP3, 3(c)(i) MP2–4, 3(d)(i) MP4–7; D10 algorithm safeguards."""
    tree = ast.parse(candidate_path.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else getattr(node.func, "attr", "")
            assert name not in {"sort", "sorted", "index", "count", "max", "min", "bisect_left", "bisect_right", "insort"}
        if isinstance(node, ast.Compare):
            assert not any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops)


def test_3bii_3cii_3dii_traced_calls_and_results(candidate_path):
    """9618_s24_42:3(b)(ii) MP1–2, 3(c)(ii) whole, 3(d)(ii) MP1–2; MS pp.32,36,39."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path)
    assert r.error is None
    recursive = r.called("RecursiveInsertion")
    iterative = r.called("IterativeInsertion")
    search = r.called("BinarySearch")
    assert recursive and iterative and search
    for call in (recursive[0], iterative[0]):
        assert call.args["IntegerArray"] == ORIGINAL
        if "NumberElements" in call.args:
            assert call.args["NumberElements"] == 7
        assert call.result == sorted(ORIGINAL)
    assert search[0].args == {"IntegerArray": sorted(ORIGINAL), "First": 0, "Last": 6, "ToFind": 644}
    assert search[0].result == 6
    assert r.calls.index(recursive[0]) < r.calls.index(iterative[0]) < r.calls.index(search[0])
    assert 6 in numbers(r.stdout)
