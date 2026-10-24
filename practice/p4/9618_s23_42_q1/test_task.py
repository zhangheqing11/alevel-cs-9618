"""9618_s23_42 Question 1 (Animals, SortDescending): tests from the exact matching MS.

1(b) is checked by running the main program in-process and taking a copy of the global Animals at
the moment SortDescending() is called (sys.setprofile), so the order the names were stored in is
visible even though the program sorts them afterwards.
"""
import runpy
import sys

import pytest

from testkit import run_script

GIVEN = ["horse", "lion", "rabbit", "mouse", "bird", "deer", "whale", "elephant", "kangaroo", "tiger"]
SORTED = ["whale", "tiger", "rabbit", "mouse", "lion", "kangaroo", "horse", "elephant", "deer", "bird"]


def run_main_capturing_sort(candidate_path, monkeypatch, tmp_path):
    """Run the program as __main__; return (copy of Animals when SortDescending was called, globals)."""
    monkeypatch.chdir(tmp_path)
    seen = []

    def profiler(frame, event, arg):
        if event == "call" and frame.f_code.co_name == "SortDescending" and not seen:
            seen.append(list(frame.f_globals.get("Animals", [])))

    sys.setprofile(profiler)
    try:
        g = runpy.run_path(str(candidate_path), run_name="__main__")
    finally:
        sys.setprofile(None)
    return (seen[0] if seen else None), g


# ---------------------------------------------------------------- 1(a)

def test_1a_global_array_animals_10_elements(sol):
    """9618_s23_42:1(a) MP1-MP2: global array named Animals with 10 elements (built as a real list, D10)."""
    assert isinstance(getattr(sol, "Animals", None), list), "no global list called Animals"
    assert len(sol.Animals) == 10


# ---------------------------------------------------------------- 1(b)

def test_1b_ten_names_stored_in_order(candidate_path, monkeypatch, tmp_path, capsys):
    """9618_s23_42:1(b) MP1-MP2: all 10 names, lower case, in the order given (checked before sorting)."""
    before, g = run_main_capturing_sort(candidate_path, monkeypatch, tmp_path)
    assert before is not None, "the main program never called SortDescending()"
    assert before == GIVEN


# ---------------------------------------------------------------- 1(c)

def _sort(sol, names):
    sol.Animals = list(names)
    sol.SortDescending()
    return sol.Animals


def test_1c_sorts_given_animals_descending(sol):
    """9618_s23_42:1(c) MP1, MP3: completed statements -- descending order of the first character."""
    assert _sort(sol, GIVEN) == SORTED


def test_1c_already_sorted_and_reversed(sol):
    """9618_s23_42:1(c) MP1, MP3: every pass and every pair (including the last one) is compared."""
    assert _sort(sol, SORTED) == SORTED
    assert _sort(sol, list(reversed(SORTED))) == SORTED


def test_1c_only_first_character_compared(sol):
    """9618_s23_42:1(c) MP2: MID(Animals[Y], 0, 1) -- names with the same first letter keep their order."""
    names = ["bat", "bear", "cow", "ant", "yak", "zebra", "fox", "gnu", "hen", "eel"]
    assert _sort(sol, names) == ["zebra", "yak", "hen", "gnu", "fox", "eel", "cow", "bat", "bear", "ant"]


# ---------------------------------------------------------------- 1(d)

def test_1d_ii_screenshot_sorted_names(candidate_path):
    """9618_s23_42:1(d)(i) MP1-MP3 and 9618_s23_42:1(d)(ii) MP1: whale ... bird, one per line (MS p.10 example)."""
    res = run_script(candidate_path)
    assert res.returncode == 0, res.stderr[-600:]
    lines = [ln.strip() for ln in res.lines]
    remaining = iter(lines)
    assert all(any(name == line for line in remaining) for name in SORTED), f"sorted names not output one per line: {lines}"


def test_1di_traced_sort(candidate_path):
    """9618_s23_42:1(d)(i) MP1; MS p.9: call SortDescending before output."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path)
    assert r.error is None
    assert r.called("SortDescending")
    remaining = iter(r.stdout.splitlines())
    assert all(any(name == line.strip() for line in remaining) for name in SORTED)
