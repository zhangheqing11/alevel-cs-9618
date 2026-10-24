"""9618_s23_41 Question 1 (DataArray, PrintArray, LinearSearch): tests from the exact matching MS.

The main program is run in-process with runpy (input() fed by the test) so the test can look at the
local array DataArray, and as a script with run_script for the screenshot cells.
"""
import re
import runpy

import pytest

from testkit import feed_input, output_lines, run_script, use_files

DATA = [10, 4, 5, 13, 25, 31, 4, 66, 12, 5, 0, 11, 15, 20, 21, 12, 33, 49, 12, 12, 7, 7, 4, 22, 0]


def run_main(candidate_path, monkeypatch, tmp_path, files_dir, *answers):
    """Run the candidate as __main__ in a copy of files/; returns its global namespace."""
    use_files(monkeypatch, tmp_path, files_dir)
    feed_input(monkeypatch, *answers)
    import sys
    seen = {}
    def profile(frame, event, arg):
        if (event == "return" and frame.f_code.co_filename == str(candidate_path)
                and frame.f_code.co_name not in ("PrintArray", "LinearSearch")
                and "DataArray" in frame.f_locals):
            seen["DataArray"] = list(frame.f_locals["DataArray"])
    old = sys.getprofile()
    try:
        sys.setprofile(profile)
        namespace = runpy.run_path(str(candidate_path), run_name="__main__")
    finally:
        sys.setprofile(old)
    namespace.update(seen)
    return namespace


def ints(line):
    return [int(v) for v in re.findall(r"-?\d+", line)]


# ---------------------------------------------------------------- 1(a)

def test_1a_dataarray_holds_25_integers_from_file(candidate_path, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s23_41:1(a)(i) MP1 and 9618_s23_41:1(a)(ii) MP1-MP3: DataArray = the 25 integers of Data.txt."""
    g = run_main(candidate_path, monkeypatch, tmp_path, exercise_dir / "files", "12")
    assert "DataArray" in g, "no array called DataArray in the main program"
    assert list(g["DataArray"]) == DATA


def test_1a_missing_file_handled(candidate_path):
    """9618_s23_41:1(a)(ii) MP4: exception handling -- no crash when Data.txt is missing."""
    res = run_script(candidate_path, stdin="12\n")  # no files copied
    assert "Traceback" not in res.stderr, res.stderr[-600:]
    assert res.returncode == 0


# ---------------------------------------------------------------- 1(b)

def test_1b_i_print_array_one_line_in_order(sol, capsys):
    """9618_s23_41:1(b)(i) MP2-MP3: all elements, in stored order, on one line."""
    sol.PrintArray([10, 4, 5, 13, 25])
    lines = output_lines(capsys.readouterr().out)
    assert any([10, 4, 5, 13, 25] == ints(line)[-5:] for line in lines)


def test_1b_i_print_array_any_length(sol, capsys):
    """9618_s23_41:1(b)(i) MP2: loops through the whole parameter array (25 elements)."""
    sol.PrintArray(DATA)
    lines = output_lines(capsys.readouterr().out)
    assert any(ints(line)[-25:] == DATA for line in lines)


def test_1b_iii_screenshot_array_output(candidate_path, exercise_dir):
    """9618_s23_41:1(b)(ii) MP1 and 9618_s23_41:1(b)(iii) MP1: the 25 values on one line (MS p.8 example)."""
    res = run_script(candidate_path, stdin="12\n", files_dir=exercise_dir / "files")
    assert res.returncode == 0, res.stderr[-600:]
    assert any(ints(ln)[-25:] == DATA for ln in res.lines), "the 25 values of Data.txt are not output on one line"


# ---------------------------------------------------------------- 1(c)

@pytest.mark.parametrize("value,count", [(12, 4), (7, 2), (0, 2), (10, 1), (99, 0)])
def test_1c_linear_search_counts(sol, value, count):
    """9618_s23_41:1(c) MP2-MP3: counts every occurrence (first and last element too) and returns the count."""
    assert sol.LinearSearch(list(DATA), value) == count


def test_1c_linear_search_other_array(sol):
    """9618_s23_41:1(c) MP2: works on the array parameter, not a global."""
    assert sol.LinearSearch([3, 3, 3], 3) == 3


# ---------------------------------------------------------------- 1(d)

def _result_line(res, number, times):
    pat = re.compile(rf"The number\s+{number}\s+is found\s+{times}\s+times")
    return bool(pat.search(res.stdout))


def test_1d_i_validates_0_to_100(candidate_path, exercise_dir):
    """9618_s23_41:1(d)(i) MP1-MP4: -1 and 101 rejected, 12 accepted, result output in the QP format."""
    res = run_script(candidate_path, stdin="-1\n101\n12\n", files_dir=exercise_dir / "files")
    assert res.returncode == 0, "crashed or asked for more input than given:\n" + res.stderr[-600:]
    assert _result_line(res, 12, 4)


@pytest.mark.parametrize("value,times", [("0", 2), ("100", 0)])
def test_1d_i_bounds_inclusive(candidate_path, exercise_dir, value, times):
    """9618_s23_41:1(d)(i) MP2: 0 and 100 are valid (inclusive)."""
    res = run_script(candidate_path, stdin=f"{value}\n", files_dir=exercise_dir / "files")
    assert res.returncode == 0, f"{value} rejected (asked again):\n" + res.stderr[-300:]
    assert _result_line(res, int(value), times)


def test_1d_ii_screenshot_number_12(candidate_path, exercise_dir):
    """9618_s23_41:1(d)(ii) MP1: input 12 -> 'The number 12 is found 4 times' (MS p.11 example)."""
    res = run_script(candidate_path, stdin="12\n", files_dir=exercise_dir / "files")
    assert res.returncode == 0, res.stderr[-600:]
    assert _result_line(res, 12, 4)


def test_1bii_1di_traced_main(candidate_path, exercise_dir):
    """9618_s23_41:1(b)(ii) whole; 1(d)(i) MP3–4; MS pp.8,10."""
    from testkit import run_script_traced
    for value in (12, 7, 99):
        r = run_script_traced(candidate_path, stdin=f"{value}\n", files_dir=exercise_dir / "files")
        assert r.error is None
        positions = {id(call): index for index, call in enumerate(r.calls)}
        prints, searches = r.called("PrintArray"), r.called("LinearSearch")
        assert prints and searches
        assert DATA in list(prints[0].args.values())
        assert list(searches[0].args.values()) == [DATA, value]
        assert positions[id(prints[0])] < positions[id(searches[0])]
        assert searches[0].result == DATA.count(value)
        assert re.search(rf"The number\s+{value}\s+is found\s+{searches[0].result}\s+times", r.stdout)
