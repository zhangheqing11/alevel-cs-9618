import runpy
import re
from testkit import feed_input, run_script, use_files

def test_3a_private_constructor(sol):
    """9618_s22_42:3(a) MP3, MP5: private Number and Colour hold the arguments."""
    card = sol.Card(7, "purple")
    assert vars(card)["_Card__Number"] == 7
    assert vars(card)["_Card__Colour"] == "purple"

def test_3b_both_getters(sol):
    """9618_s22_42:3(b) MP2-MP3: both attributes returned without alteration."""
    card = sol.Card(10, "orange")
    assert card.GetNumber() == 10
    assert card.GetColour() == "orange"

def test_3c_reads_all_cards_and_3e_player(sol, candidate_path, exercise_dir, monkeypatch, tmp_path, capsys):
    """9618_s22_42:3(c) MP1-MP7; 3(e)(i) MP1-MP5: all file pairs and four selected objects."""
    work = use_files(monkeypatch, tmp_path, exercise_dir / "files")
    feed_input(monkeypatch, "1", "5", "9", "30")
    ns = runpy.run_path(str(candidate_path), run_name="__main__")
    data = (work / "CardValues.txt").read_text().splitlines()
    cards = ns["CardArray"]
    assert len(cards) == 30
    assert [(c.GetNumber(), c.GetColour().strip()) for c in cards] == [(int(data[i]), data[i+1]) for i in range(0,60,2)]
    assert len(ns["Player1"]) == 4
    assert [c.GetNumber() for c in ns["Player1"]] == [1,9,9,10]

def test_3c_missing_file_message(candidate_path, monkeypatch, tmp_path, capsys):
    """9618_s22_42:3(c) MP8-MP9: missing file is caught with an output message."""
    monkeypatch.chdir(tmp_path)
    feed_input(monkeypatch, "1", "2", "3", "4")
    # Stop after the file-loading stage, before uninitialised cards can be used.
    import sys
    class StopAfterRead(Exception): pass
    def trace(frame, event, arg):
        if frame.f_code.co_filename == str(candidate_path) and event == "line":
            cards = frame.f_globals.get("Player1")
            if cards is not None: raise StopAfterRead
        return trace
    previous = sys.gettrace()
    try:
        sys.settrace(trace)
        try: runpy.run_path(str(candidate_path), run_name="__main__")
        except StopAfterRead: pass
    finally: sys.settrace(previous)
    assert capsys.readouterr().out.strip()

def test_3d_validation_and_duplicate_rejection(candidate_path, exercise_dir, monkeypatch, tmp_path, capsys):
    """9618_s22_42:3(d) MP1-MP9: any suitable selection store; inclusive bounds and persistent choices."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    # Run the required setup without dictating a flag array or its name.
    feed_input(monkeypatch, "1", "2", "3", "4", "0", "31", "1", "30", "30", "29")
    ns = runpy.run_path(str(candidate_path), run_name="__main__")
    choose = ns["ChooseCard"]
    assert choose() == 29
    assert choose() == 28


def test_3e_ii_both_screenshots(candidate_path, exercise_dir):
    """9618_s22_42:3(e)(ii) whole: both official selections, repeats rejected."""
    for inputs, expected in [("1\n5\n9\n10\n", ["red", "1", "green", "9", "orange", "9", "red", "10"]), ("2\n2\n3\n4\n4\n5\n", ["black", "5", "white", "2", "red", "4", "green", "9"])]:
        result = run_script(candidate_path, stdin=inputs, files_dir=exercise_dir / "files")
        assert result.returncode == 0, result.stderr
        # Number/colour may be printed on one line or separate lines, in either order.
        words = re.findall(r"[A-Za-z]+|[0-9]+", result.stdout.lower())
        pos = 0
        for colour, number in zip(expected[::2], expected[1::2]):
            for i in range(pos, len(words)-1):
                if words[i:i+2] in ([colour,number], [number,colour]): pos=i+2; break
            else: raise AssertionError((colour,number,result.stdout))


def test_3main_call_chain(candidate_path, exercise_dir):
    """9618_s22_42:3(e)(i) MS p.34: observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='1\n5\n9\n30\n', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    choices = r.called("ChooseCard")
    assert [c.result for c in choices] == [0,4,8,29]
    assert len(r.called("GetNumber")) >= 4 and len(r.called("GetColour")) >= 4
    assert all(str(c.result) in r.stdout for c in r.called("GetNumber") + r.called("GetColour"))
