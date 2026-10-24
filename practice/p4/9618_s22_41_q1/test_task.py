"""9618_s22_41 Question 1 (HighScore): tests derived from the exact matching MS (9618/41 May/June 2022).

Function-style tests call the QP module names (ReadHighScores, OutputHighScores, WriteTopTen) and the
MS name Arrange(Username, Score) for the unnamed 1(e)(ii) procedure. Screenshot cells run the whole
program with run_script and look for the values the MS lists, line by line (prompts may share a line).
"""
import re

from testkit import output_lines, run_script, use_files

ORIGINAL = ["FYI 10000", "ABC 9092", "KEL 8500", "PAI 8203", "BBB 7980",
            "ACE 7246", "GKL 7001", "JSI 6490", "EIF 6003", "DIS 2000"]
WITH_JKL = ["FYI 10000", "JKL 9999", "ABC 9092", "KEL 8500", "PAI 8203",
            "BBB 7980", "ACE 7246", "GKL 7001", "JSI 6490", "EIF 6003"]


def find_block(lines, block, start=0):
    """Index of the first run of consecutive lines ending with the block's items, or -1."""
    for i in range(start, len(lines) - len(block) + 1):
        if all(lines[i + k].rstrip().endswith(block[k]) for k in range(len(block))):
            return i
    return -1


def printed(capsys):
    return [ln.strip() for ln in output_lines(capsys.readouterr().out)]


def tokens(text):
    return [t for t in re.split(r"[\s,]+", text) if t]


def run(candidate_path, exercise_dir, stdin):
    return run_script(candidate_path, stdin=stdin, files_dir=exercise_dir / "files")


# ---------------------------------------------------------------- 1(a)

def test_1a_global_array_has_11_elements(sol):
    """9618_s22_41:1(a) MP1-MP2: at least one global array, 11 elements."""
    def has_11(v):
        return isinstance(v, list) and (len(v) == 11 or any(isinstance(e, list) and len(e) == 11 for e in v))
    assert any(has_11(v) for v in vars(sol).values()), "no global list with 11 elements"


# ---------------------------------------------------------------- 1(b) / 1(c)

def test_1b_reads_ten_players_from_file(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s22_41:1(b) MP2-MP5 (open, loop 10 pairs, read each pair, store name and score)."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    sol.ReadHighScores()
    capsys.readouterr()
    sol.OutputHighScores()
    lines = printed(capsys)
    assert lines[:10] == ORIGINAL


def test_1b_missing_file_handled(sol, monkeypatch, tmp_path, capsys):
    """9618_s22_41:1(b) MP7-MP8: exception handling on the file with an output message."""
    monkeypatch.chdir(tmp_path)  # empty directory: HighScore.txt is missing
    sol.ReadHighScores()
    assert capsys.readouterr().out.strip(), "no message when HighScore.txt is missing"


def test_1c_outputs_every_element_name_space_score(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s22_41:1(c) MP2-MP3: all elements, 'PlayerName Score', each player on a new line."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    sol.ReadHighScores()
    capsys.readouterr()
    sol.OutputHighScores()
    lines = printed(capsys)
    assert len(lines) in (10, 11), f"expected the 10 players (+ the empty 11th element), got {len(lines)} lines"
    for ln in lines[:10]:
        assert re.fullmatch(r"[A-Z]{3} \d+", ln), f"line not in the format 'PlayerName Score': {ln!r}"


# ---------------------------------------------------------------- 1(d)

def test_1d_screenshot_shows_ten_players(candidate_path, exercise_dir):
    """9618_s22_41:1(d)(i) MP1-MP2 and 9618_s22_41:1(d)(ii) MP1: the 10 names and scores from the file."""
    res = run(candidate_path, exercise_dir, "JKL\n9999\n")
    assert res.returncode == 0, res.stderr[-500:]
    assert find_block(res.lines, ORIGINAL) >= 0, "the 10 players from HighScore.txt are not output in order"


# ---------------------------------------------------------------- 1(e)(i)

def test_1e_i_rejects_name_not_3_characters(candidate_path, exercise_dir):
    """9618_s22_41:1(e)(i) MP1-MP2: ABCD and AB are rejected, JKL is accepted."""
    res = run(candidate_path, exercise_dir, "ABCD\nAB\nJKL\n9999\n")
    assert res.returncode == 0, "program crashed or asked for more input than given:\n" + res.stderr[-500:]
    assert find_block(res.lines, WITH_JKL) >= 0


def test_1e_i_score_upper_bound_100000_inclusive(candidate_path, exercise_dir):
    """9618_s22_41:1(e)(i) MP3: 100001 rejected, 100000 accepted."""
    res = run(candidate_path, exercise_dir, "ABC\n100001\n100000\n")
    assert res.returncode == 0, res.stderr[-500:]
    assert not any(ln.rstrip().endswith("100001") for ln in res.lines), "100001 was accepted"
    assert find_block(res.lines, ["ABC 100000", "FYI 10000"]) >= 0


def test_1e_i_score_lower_bound(candidate_path, exercise_dir):
    """9618_s22_41:1(e)(i) MP3: 0 rejected; 1 accepted without asking again."""
    res = run(candidate_path, exercise_dir, "ABC\n0\n2500\n")
    assert res.returncode == 0, res.stderr[-500:]
    assert find_block(res.lines, ["EIF 6003", "ABC 2500"]) >= 0, "0 was accepted (2500 never read)"
    res = run(candidate_path, exercise_dir, "ABC\n1\n")
    assert res.returncode == 0, "score 1 must be accepted (1 to 100000 inclusive):\n" + res.stderr[-300:]


# ---------------------------------------------------------------- 1(e)(ii)

def _arranged(sol, monkeypatch, tmp_path, exercise_dir, capsys, name, score):
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    sol.ReadHighScores()
    sol.Arrange(name, score)
    capsys.readouterr()
    sol.OutputHighScores()
    return printed(capsys)


def test_1e_ii_inserts_jkl_in_second_place(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s22_41:1(e)(ii) MP2-MP5: find the position, move the rest down, store name and score."""
    lines = _arranged(sol, monkeypatch, tmp_path, exercise_dir, capsys, "JKL", 9999)
    assert lines[:10] == WITH_JKL


def test_1e_ii_inserts_at_top(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s22_41:1(e)(ii) MP3-MP5: new highest score goes first, everything else moves down."""
    lines = _arranged(sol, monkeypatch, tmp_path, exercise_dir, capsys, "TOP", 100000)
    assert lines[:10] == ["TOP 100000"] + ORIGINAL[:9]


def test_1e_ii_inserts_in_tenth_place(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s22_41:1(e)(ii) MP2-MP3: the loop reaches the last of the top ten."""
    lines = _arranged(sol, monkeypatch, tmp_path, exercise_dir, capsys, "LOW", 2001)
    assert lines[:10] == ORIGINAL[:9] + ["LOW 2001"]


def test_1e_ii_score_too_low_not_inserted(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s22_41:1(e)(ii) MP3: 'if appropriate' -- a score below the top ten leaves it unchanged."""
    lines = _arranged(sol, monkeypatch, tmp_path, exercise_dir, capsys, "BAD", 1500)
    assert lines[:10] == ORIGINAL


# ---------------------------------------------------------------- 1(e)(iii) / (iv)

def test_1e_iv_screenshot_before_and_after(candidate_path, exercise_dir):
    """9618_s22_41:1(e)(iii) MP1-MP2 and 9618_s22_41:1(e)(iv) MP1: JKL 9999 entered, after shows JKL second."""
    res = run(candidate_path, exercise_dir, "JKL\n9999\n")
    assert res.returncode == 0, res.stderr[-500:]
    before = find_block(res.lines, ORIGINAL)
    assert before >= 0, "array not output before inserting"
    assert find_block(res.lines, WITH_JKL, before + 1) > before, "array after inserting JKL 9999 not output"


# ---------------------------------------------------------------- 1(f)

def test_1f_writes_new_top_ten(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_s22_41:1(f) MP1, MP3-MP4: NewHighScore.txt holds the 10 names then scores, DIS dropped."""
    work = use_files(monkeypatch, tmp_path, exercise_dir / "files")
    sol.ReadHighScores()
    sol.Arrange("JKL", 9999)
    sol.WriteTopTen()
    text = (work / "NewHighScore.txt").read_text(encoding="utf-8")
    assert tokens(text) == tokens(" ".join(WITH_JKL))


def test_1f_writes_unchanged_top_ten(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_s22_41:1(f) MP3-MP4: all 10 array values written (no insertion)."""
    work = use_files(monkeypatch, tmp_path, exercise_dir / "files")
    sol.ReadHighScores()
    sol.WriteTopTen()
    text = (work / "NewHighScore.txt").read_text(encoding="utf-8")
    assert tokens(text) == tokens(" ".join(ORIGINAL))


def test_1di_eiii_traced_main(candidate_path, exercise_dir):
    """9618_s22_41:1(d)(i) MP1–2; 1(e)(iii) MP1–2; MS pp.8,15."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin="JKL\n9999\n", files_dir=exercise_dir / "files")
    assert r.error is None
    read, output, arrange = r.called("ReadHighScores"), r.called("OutputHighScores"), r.called("Arrange")
    assert read and len(output) >= 2 and arrange
    assert list(arrange[0].args.values()) == ["JKL", 9999]
    assert next(i for i, c in enumerate(r.calls) if c is read[0]) < next(i for i, c in enumerate(r.calls) if c is output[0]) < next(i for i, c in enumerate(r.calls) if c is arrange[0]) < next(i for i, c in enumerate(r.calls) if c is output[-1])
    assert find_block(r.stdout.splitlines(), ORIGINAL) >= 0
    assert find_block(r.stdout.splitlines(), WITH_JKL) >= 0
