"""Tests for 9618_w24_42 Question 3 (HighScoreTable.txt: 2D array, read, output, two-key bubble sort).

Mark point numbers are corpus markpoints[].n (they match the MS bullets here).
"""
import builtins
import copy
import io
import runpy
import sys

from testkit import output_lines, run_script, use_files

DATA_FILE = "HighScoreTable.txt"
# QP 3(d) example table, positions 1-7 (already in the required order)
QP_TABLE = [["GFED", "5", "25"], ["HJKM", "4", "21"], ["RERR", "4", "19"], ["TTYU", "4", "15"],
            ["WSVG", "3", "20"], ["PPTR", "3", "15"], ["SNQT", "2", "10"]]


def official_rows(exercise_dir):
    lines = (exercise_dir / "files" / DATA_FILE).read_text().splitlines()
    return [lines[i:i + 3] for i in range(0, 21, 3)]


def required_order(rows):
    """Level descending, then score descending (numeric)."""
    return sorted(rows, key=lambda r: (-int(r[1]), -int(r[2])))


def sentence(row):
    return f"{row[0]} reached level {row[1]} with a score of {row[2]}"


def normalise(lines):
    return [" ".join(line.split()) for line in lines]


def as_rows(array):
    return [[str(v) for v in r] for r in array]


def watch_open(monkeypatch):
    real_open = builtins.open
    handles = []

    def tracked(*args, **kwargs):
        handle = real_open(*args, **kwargs)
        handles.append(handle)
        return handle

    monkeypatch.setattr(builtins, "open", tracked)
    monkeypatch.setattr(io, "open", tracked)
    return handles


def values_of_highscores_in_main(path):
    """Run the program as __main__ in-process and record every value the main program's
    HighScores takes (snapshots at each line), skipping the subroutines' own locals."""
    filename = str(path)
    seen = []
    skip = {"ReadData", "SortScores", "OutputHighScores"}

    def local_tracer(frame, event, arg):
        value = frame.f_locals.get("HighScores")
        if isinstance(value, list) and (not seen or seen[-1] != value):
            seen.append(copy.deepcopy(value))
        return local_tracer

    def global_tracer(frame, event, arg):
        if frame.f_code.co_filename == filename and frame.f_code.co_name not in skip:
            return local_tracer
        return None

    sys.settrace(global_tracer)
    try:
        runpy.run_path(filename, run_name="__main__")
    finally:
        sys.settrace(None)
    return seen


# ---------------------------------------------------------------- 3(a)

def test_3a_highscores_7_by_3_empty_strings(candidate_path, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_w24_42:3(a) MP1-MP2: the main program's HighScores is a 7 x 3 array with every element "" before ReadData()."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    seen = values_of_highscores_in_main(candidate_path)
    capsys.readouterr()
    empty = [["", "", ""] for _ in range(7)]
    assert any(as_rows(v) == empty for v in seen if len(v) == 7 and all(len(r) == 3 for r in v)), \
        "HighScores is never a 7 x 3 array of empty strings in the main program"


# ---------------------------------------------------------------- 3(b)

def test_3b_readdata_returns_7_players_of_3_strings(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w24_42:3(b) MP1-MP4: 7 groups of 3 lines, each item (newline removed) in its own element, array returned."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    result = sol.ReadData()
    assert [list(r) for r in result] == official_rows(exercise_dir)
    assert all(isinstance(v, str) for r in result for v in r), "all data is stored as strings (QP 3(a))"


def test_3b_readdata_closes_file(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w24_42:3(b) MP2: the file is opened for reading and closed."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    handles = watch_open(monkeypatch)
    sol.ReadData()
    assert handles, "ReadData() did not open a file"
    assert all(h.closed for h in handles), "HighScoreTable.txt is left open"


def test_3b_missing_file_is_handled(sol, monkeypatch, tmp_path, capsys):
    """9618_w24_42:3(b) MP5: exception handling with an output when the file is missing."""
    monkeypatch.chdir(tmp_path)  # empty folder: no HighScoreTable.txt
    sol.ReadData()
    assert capsys.readouterr().out.strip(), "no message was output for the missing file"


# ---------------------------------------------------------------- 3(c)

def test_3c_output_format_in_array_order(sol, capsys):
    """9618_w24_42:3(c) MP1-MP2: one line per player, in array order, 'GHEH reached level 3 with a score of 10'."""
    sol.OutputHighScores([list(r) for r in QP_TABLE])
    assert normalise(output_lines(capsys.readouterr().out)) == [sentence(r) for r in QP_TABLE]


# ---------------------------------------------------------------- 3(d)

def test_3d_sortscores_official_data(sol, exercise_dir):
    """9618_w24_42:3(d) MP1-MP4: level descending, then score descending; whole rows move together."""
    rows = official_rows(exercise_dir)
    assert as_rows(sol.SortScores([list(r) for r in rows])) == required_order(rows)


def test_3d_sortscores_qp_example_from_reverse(sol):
    """9618_w24_42:3(d) MP2-MP4: the QP example table, given in reverse, is sorted back into positions 1-7."""
    assert as_rows(sol.SortScores([list(r) for r in reversed(QP_TABLE)])) == QP_TABLE


def test_3d_sortscores_compares_numbers_not_text(sol):
    """9618_w24_42:3(d) MP3: scores compared as numbers (15 beats 9 on the same level)."""
    rows = [["AAAA", "4", "9"], ["BBBB", "4", "15"], ["CCCC", "3", "30"]]
    assert as_rows(sol.SortScores([list(r) for r in rows])) == [["BBBB", "4", "15"], ["AAAA", "4", "9"], ["CCCC", "3", "30"]]


# ---------------------------------------------------------------- 3(e)

def test_3e_screenshot_before_and_after(candidate_path, exercise_dir):
    """9618_w24_42:3(e)(ii) MP1-MP2 (and 3(e)(i) MP1-MP2): 'Before' + file order, then 'After' + sorted order."""
    result = run_script(candidate_path, files_dir=exercise_dir / "files")
    assert result.returncode == 0, result.stderr
    rows = official_rows(exercise_dir)
    expected = ["Before"] + [sentence(r) for r in rows] + ["After"] + [sentence(r) for r in required_order(rows)]
    assert normalise(result.lines) == expected
