"""Tests for 9618_w23_42 Question 2 (total of divisors: iterative, then recursive with gaps).

Mark point numbers are corpus markpoints[].n. In 2(b)(i) corpus MP1 is the MS line
"One mark for each gap (5)" (5 marks), MP2 = recursive calls, MP3 = remainder.
"""
import re

import pytest

from testkit import run_script

DIVISOR_TOTALS = [(10, 18), (4, 7), (1, 1), (7, 8), (12, 28), (50, 93)]


def ints(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]


def is_subsequence(wanted, seen):
    it = iter(seen)
    return all(any(w == s for s in it) for w in wanted)


def count_calls(monkeypatch, sol, name):
    """Wrap sol.<name>; recursive calls go through the module global, so they are counted."""
    original = getattr(sol, name)
    calls = []

    def spy(*args):
        calls.append(args)
        return original(*args)

    monkeypatch.setattr(sol, name, spy)
    return spy, calls


# ---------------------------------------------------------------- 2(a)

@pytest.mark.parametrize("number, total", DIVISOR_TOTALS)
def test_2a_iterativecalculate_totals_divisors(sol, number, total):
    """9618_w23_42:2(a)(i) MP2-MP4: loop from Number down to 1, MODULUS test, total returned."""
    assert sol.IterativeCalculate(number) == total


def test_2a_iterativecalculate_is_iterative(sol, monkeypatch):
    """9618_w23_42:2(a)(i) MP2 (partial): called once, no recursion; MP5 full structure is checked manually."""
    spy, calls = count_calls(monkeypatch, sol, "IterativeCalculate")
    assert spy(10) == 18
    assert len(calls) == 1


def test_2a_screenshot_outputs_18(candidate_path):
    """9618_w23_42:2(a)(iii) MP-03 (and 2(a)(ii) MP1-MP2): IterativeCalculate(10) is output: 18."""
    result = run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    assert 18 in ints(result.stdout)


# ---------------------------------------------------------------- 2(b)

@pytest.mark.parametrize("number, total", DIVISOR_TOTALS)
def test_2b_recursivevalue_totals_divisors(sol, number, total):
    """9618_w23_42:2(b)(i) MP1 (gaps 0, MODULUS, Number), MP3: RecursiveValue(n, n) totals the divisors of n."""
    assert sol.RecursiveValue(number, number) == total


def test_2b_recursivevalue_keeps_tofind(sol):
    """9618_w23_42:2(b)(i) MP1 (gaps RETURN, ToFind), MP2: ToFind is passed on unchanged.
    RecursiveValue(5, 10) adds only the divisors of 10 that are <= 5: 1 + 2 + 5."""
    assert sol.RecursiveValue(5, 10) == 8
    assert sol.RecursiveValue(0, 10) == 0


def test_2b_recursivevalue_is_recursive(sol, monkeypatch):
    """9618_w23_42:2(b)(i) MP2: one recursive call for each Number from 10 down to the base case 0."""
    spy, calls = count_calls(monkeypatch, sol, "RecursiveValue")
    assert spy(10, 10) == 18
    assert [c[0] for c in calls] == list(range(10, -1, -1))
    assert all(c[1] == 10 for c in calls)


def test_2b_screenshot_outputs_93(candidate_path):
    """9618_w23_42:2(b)(iii) MP-03 (and 2(b)(ii)): after the 18 from 2(a), RecursiveValue(50, 50) is output: 93."""
    result = run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    assert is_subsequence([18, 93], ints(result.stdout))


def test_2aii_2bii_traced_main(candidate_path):
    """9618_w23_42:2(a)(ii) MP1–2; 2(b)(ii) whole; MS pp.18,21."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path)
    assert r.error is None
    iterative, recursive = r.called("IterativeCalculate"), r.called("RecursiveValue")
    assert iterative and recursive
    assert iterative[0].args == {"Number": 10} and iterative[0].result == 18
    assert recursive[0].args == {"Number": 50, "ToFind": 50} and recursive[0].result == 93
    assert next(i for i, c in enumerate(r.calls) if c is iterative[0]) < next(i for i, c in enumerate(r.calls) if c is recursive[0])
    assert is_subsequence([iterative[0].result, recursive[0].result], ints(r.stdout))
