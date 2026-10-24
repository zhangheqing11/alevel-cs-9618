"""Tests for 9618_w24_41 Question 1 (Data.txt colours: read, format, compare, bubble sort).

Mark point numbers are corpus markpoints[].n (they match the MS bullets here).
"""
import builtins
import io

import pytest

from testkit import run_script, use_files

DATA_FILE = "Data.txt"


def official_items(exercise_dir):
    return (exercise_dir / "files" / DATA_FILE).read_text().splitlines()


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


class WholeStringCompareForbidden(str):
    """A str whose whole-string <, >, <=, >= raise; single characters (s[i]) are plain str."""

    def _forbidden(self, other):
        raise AssertionError("compare one character at a time, not the whole strings (QP 1(c))")

    __lt__ = __gt__ = __le__ = __ge__ = _forbidden


def count_calls(monkeypatch, sol, name):
    original = getattr(sol, name)
    calls = []

    def spy(*args):
        calls.append(args)
        return original(*args)

    monkeypatch.setattr(sol, name, spy)
    return calls


# ---------------------------------------------------------------- 1(a)

def test_1a_readdata_returns_all_45_items(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w24_41:1(a) MP2-MP6: 45-item array, every line read (newline removed) and stored, array returned."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    result = sol.ReadData()
    assert list(result) == official_items(exercise_dir)


def test_1a_readdata_closes_file(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w24_41:1(a) MP3: Data.txt is opened for reading and closed."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    handles = watch_open(monkeypatch)
    sol.ReadData()
    assert handles, "ReadData() did not open a file"
    assert all(h.closed for h in handles), "Data.txt is left open"


def test_1a_missing_file_is_handled(sol, monkeypatch, tmp_path, capsys):
    """9618_w24_41:1(a) MP7: try / except with an output when Data.txt is missing."""
    monkeypatch.chdir(tmp_path)  # empty folder: no Data.txt
    sol.ReadData()
    assert capsys.readouterr().out.strip(), "no message was output for the missing file"


# ---------------------------------------------------------------- 1(b)

def test_1b_formatarray_joins_with_spaces(sol, exercise_dir):
    """9618_w24_41:1(b)(i) MP1-MP2: every element concatenated with a space between, string returned."""
    items = official_items(exercise_dir)
    result = sol.FormatArray(list(items))
    assert isinstance(result, str)
    assert result.strip() == " ".join(items)


def test_1b_screenshot_all_colours_in_one_string(candidate_path, exercise_dir):
    """9618_w24_41:1(b)(iii) MP-03 (and 1(b)(ii) MP1-MP3): the 45 colours in file order on one line."""
    result = run_script(candidate_path, files_dir=exercise_dir / "files")
    assert result.returncode == 0, result.stderr
    assert any(" ".join(official_items(exercise_dir)) in line for line in result.lines)


# ---------------------------------------------------------------- 1(c)

@pytest.mark.parametrize("first, second, expected", [
    ("apple", "banana", 1),
    ("banana", "apple", 2),
    ("magenta", "magnolia", 1),
    ("mango", "magnolia", 2),
    ("silver", "slate", 1),
    ("turquoise", "violet", 1),
    ("russet", "rose", 2),
])
def test_1c_comparestrings_returns_1_or_2(sol, first, second, expected):
    """9618_w24_41:1(c) MP1-MP4: returns 1 when the first comes first alphabetically, 2 otherwise."""
    assert sol.CompareStrings(first, second) == expected


def test_1c_compares_one_character_at_a_time(sol):
    """9618_w24_41:1(c) MP2: no whole-string comparison (QP: one character at a time)."""
    assert sol.CompareStrings(WholeStringCompareForbidden("periwinkle"), WholeStringCompareForbidden("peach")) == 2
    assert sol.CompareStrings(WholeStringCompareForbidden("mauve"), WholeStringCompareForbidden("mint")) == 1


# ---------------------------------------------------------------- 1(d)

def test_1d_bubble_sorts_official_data(sol, exercise_dir):
    """9618_w24_41:1(d)(i) MP1, MP3: the 45 colours returned in ascending alphabetical order."""
    items = official_items(exercise_dir)
    assert list(sol.Bubble(list(items))) == sorted(items)


def test_1d_bubble_reverse_order(sol, exercise_dir):
    """9618_w24_41:1(d)(i) MP3: worst case (reverse order) is fully sorted."""
    items = sorted(official_items(exercise_dir), reverse=True)
    assert list(sol.Bubble(list(items))) == sorted(items)


def test_1d_bubble_uses_comparestrings(sol, monkeypatch, exercise_dir):
    """9618_w24_41:1(d)(i) MP2: the bubble sort compares with CompareStrings()."""
    calls = count_calls(monkeypatch, sol, "CompareStrings")
    items = official_items(exercise_dir)
    assert list(sol.Bubble(list(items))) == sorted(items)
    assert len(calls) >= len(items) - 1, "Bubble() must call CompareStrings() to compare the strings"


def test_1d_screenshot_sorted_data(candidate_path, exercise_dir):
    """9618_w24_41:1(d)(iii) MP-03 (and 1(d)(ii) MP1-MP2): after the unsorted line, the sorted colours on one line."""
    result = run_script(candidate_path, files_dir=exercise_dir / "files")
    assert result.returncode == 0, result.stderr
    lines = [line.strip() for line in result.lines]
    items = official_items(exercise_dir)
    unsorted_line, sorted_line = " ".join(items), " ".join(sorted(items))
    before = next(i for i, line in enumerate(lines) if unsorted_line in line)
    assert any(sorted_line in line for line in lines[before + 1:])


def test_1bii_1dii_traced_main(candidate_path, exercise_dir):
    """9618_w24_41:1(b)(ii) MP1–3; 1(d)(ii) MP1–2; MS pp.7,11."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, files_dir=exercise_dir / "files")
    assert r.error is None
    positions = {id(call): index for index, call in enumerate(r.calls)}
    reads, formats, sorts = r.called("ReadData"), r.called("FormatArray"), r.called("Bubble")
    assert reads and len(formats) >= 2 and sorts
    items = official_items(exercise_dir)
    assert reads[0].result == items
    assert list(formats[0].args.values())[0] == reads[0].result
    assert list(sorts[0].args.values())[0] == reads[0].result
    assert sorts[0].result == sorted(items)
    assert list(formats[-1].args.values())[0] == sorts[0].result
    assert formats[0].result.strip() in r.stdout and formats[-1].result.strip() in r.stdout
    assert positions[id(reads[0])] < positions[id(formats[0])] < positions[id(sorts[0])] < positions[id(formats[-1])]
