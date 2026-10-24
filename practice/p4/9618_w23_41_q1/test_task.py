"""Tests for 9618_w23_41 Question 1 (count lower-case vowels: iterative and recursive).

Mark point numbers are corpus markpoints[].n (they match the MS bullets here).
"""
import re

import pytest

from testkit import run_script

CASES = [
    ("house", 3),
    ("imagine", 4),
    ("", 0),
    ("rhythm", 0),
    ("aeiou", 5),
    ("queue", 4),
    ("AEIOU", 0),  # only lower-case vowels are counted (QP)
    ("computer", 3),
]


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


# ---------------------------------------------------------------- 1(a)

@pytest.mark.parametrize("value, expected", CASES)
def test_1a_iterativevowels_counts(sol, value, expected):
    """9618_w23_41:1(a)(i) MP2-MP6: loop LENGTH(Value) times, check the first character, keep the remainder."""
    assert sol.IterativeVowels(value) == expected


def test_1a_iterativevowels_is_not_recursive(sol, monkeypatch):
    """9618_w23_41:1(a)(i) MP6: matches the structure of the given iterative algorithm (one call, a loop)."""
    spy, calls = count_calls(monkeypatch, sol, "IterativeVowels")
    assert spy("imagine") == 4
    assert len(calls) == 1


def test_1a_screenshot_house_outputs_3(candidate_path):
    """9618_w23_41:1(a)(iii) MP-03 (and 1(a)(ii) MP1-MP2): the program outputs 3 for "house"."""
    result = run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    assert 3 in ints(result.stdout)


# ---------------------------------------------------------------- 1(b)

@pytest.mark.parametrize("value, expected", CASES)
def test_1b_recursivevowels_counts(sol, value, expected):
    """9618_w23_41:1(b)(i) MP3-MP6: base case returns 0; vowel -> 1 + call on the rest; otherwise call on the rest."""
    assert sol.RecursiveVowels(value) == expected


def test_1b_recursivevowels_is_recursive(sol, monkeypatch):
    """9618_w23_41:1(b)(i) MP1, MP5-MP6: one recursive call per character, down to the empty string."""
    spy, calls = count_calls(monkeypatch, sol, "RecursiveVowels")
    assert spy("imagine") == 4
    assert len(calls) == len("imagine") + 1, "expected one call per character plus the base case"


def test_1b_screenshot_imagine_outputs_4(candidate_path):
    """9618_w23_41:1(b)(iii) MP-03 (and 1(b)(ii)): after the 3 from 1(a), the program outputs 4 for "imagine"."""
    result = run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    assert is_subsequence([3, 4], ints(result.stdout))


def test_1aii_1bii_traced_main(candidate_path):
    """9618_w23_41:1(a)(ii) MP1–2; 1(b)(ii) whole; MS pp.6,8."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path)
    assert r.error is None
    iterative, recursive = r.called("IterativeVowels"), r.called("RecursiveVowels")
    assert iterative and recursive
    assert iterative[0].args == {"Value": "house"} and iterative[0].result == 3
    assert recursive[0].args == {"Value": "imagine"} and recursive[0].result == 4
    assert next(i for i, c in enumerate(r.calls) if c is iterative[0]) < next(i for i, c in enumerate(r.calls) if c is recursive[0])
    assert is_subsequence([iterative[0].result, recursive[0].result], ints(r.stdout))
