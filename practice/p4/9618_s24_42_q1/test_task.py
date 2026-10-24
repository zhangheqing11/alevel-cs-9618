"""9618_s24_42 Question 1 (word game: ReadWords, Play): tests from the exact matching MS.

ReadWords() is tested with Play() replaced by a stub (1(d)(i) makes ReadWords call Play). Play() is
tested with WordArray / NumberWords set by the test and input() answered by the test; the output
produced after each input is recorded so the response to each word can be checked.
"""
import builtins
import re

import pytest

from testkit import run_script, use_files

EASY = ["hues", "hose", "hoes", "shoe", "sou", "ohs", "ose", "oes", "sue", "use", "hue", "hoe", "hes", "she"]


def answers(exercise_dir, name):
    lines = (exercise_dir / "files" / name).read_bytes().decode("ascii").split("\r\n")
    return lines[0], lines[1:]


def numbers(text):
    return [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", text)]


def has_percentage(text, expected):
    """A number within 0.05 of the expected percentage, or a whole number within 0.5 followed by %."""
    if any(abs(v - expected) < 0.05 for v in numbers(text)):
        return True
    return any(abs(float(v) - expected) < 0.5 for v in re.findall(r"(\d+)\s*%", text))


def after_percentage(lines, expected):
    for i, ln in enumerate(lines):
        if has_percentage(ln, expected):
            return lines[i + 1:]
    return None


def tokens(lines):
    return [t for ln in lines for t in re.split(r"[^A-Za-z]+", ln) if t]


# ---------------------------------------------------------------- 1(a)

@pytest.mark.parametrize("name,count", [("Easy.txt", 14), ("Medium.txt", 44), ("Hard.txt", 97)])
def test_1a_read_words_main_word_answers_and_count(sol, monkeypatch, tmp_path, exercise_dir, name, count):
    """9618_s24_42:1(a) MP2, MP4-MP7: main word in [0], each answer (newline removed) after it, NumberWords = answers."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    monkeypatch.setattr(sol, "Play", lambda: None)
    sol.ReadWords(name)
    main, words = answers(exercise_dir, name)
    assert len(words) == count
    assert sol.WordArray[0] == main
    assert list(sol.WordArray[1:count + 1]) == words
    assert sol.NumberWords == count, "NumberWords must be the number of answers (main word not counted)"


def test_1a_missing_file_handled(sol, monkeypatch, tmp_path, capsys):
    """9618_s24_42:1(a) MP3: exception handling with an output message when the file cannot be opened."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sol, "Play", lambda: None)
    sol.ReadWords("NoSuchFile.txt")
    assert capsys.readouterr().out.strip(), "no message output when the file is missing"


# ---------------------------------------------------------------- 1(c)

def play(sol, monkeypatch, capsys, words, inputs):
    """Run Play() on [main] + words; returns (output before the first input, outputs after each input)."""
    sol.WordArray = ["house"] + list(words) + [""] * (100 - 1 - len(words))
    sol.NumberWords = len(words)
    queue, chunks = list(inputs), []

    def fake_input(prompt=""):
        chunks.append(capsys.readouterr().out)
        if not queue:
            raise AssertionError("Play() asked for more input than the test provides (does 'no' stop it?)")
        return queue.pop(0)

    monkeypatch.setattr(builtins, "input", fake_input)
    sol.Play()
    chunks.append(capsys.readouterr().out)
    assert not queue, "Play() stopped before reading all the test inputs"
    return chunks[0], chunks[1:]


def test_1c_i_outputs_main_word_and_number_of_answers(sol, monkeypatch, capsys):
    """9618_s24_42:1(c)(i) MP1: outputs the main word and the number of answers (14)."""
    first, _ = play(sol, monkeypatch, capsys, EASY, ["no"])
    assert "house" in first
    assert 14 in [int(v) for v in numbers(first)]


def test_1c_i_found_and_not_found_messages(sol, monkeypatch, capsys):
    """9618_s24_42:1(c)(i) MP2, MP4: a different message for an answer (she) and a non-answer (out)."""
    _, after = play(sol, monkeypatch, capsys, EASY, ["she", "out", "no"])
    assert after[0].strip() and after[1].strip(), "no output after each word entered"
    strip_digits = lambda s: re.sub(r"\d+", "", s).strip()
    assert strip_digits(after[0]) != strip_digits(after[1]), "same message for an answer and a non-answer"


def test_1c_i_correct_answer_replaced_with_null(sol, monkeypatch, capsys):
    """9618_s24_42:1(c)(i) MP3: the answer entered is replaced with a null value; the others stay."""
    play(sol, monkeypatch, capsys, EASY, ["she", "no"])
    assert sol.WordArray[14] in ("", None)
    assert list(sol.WordArray[1:14]) == EASY[:13]
    assert sol.WordArray[0] in ("house", "", None)


def test_1c_i_main_word_is_not_an_answer(sol, monkeypatch, capsys):
    """9618_s24_42:1(c)(i) MP2: compares with each answer but not the main word (index 0)."""
    _, after = play(sol, monkeypatch, capsys, EASY, ["house", "she", "no"])
    strip_digits = lambda s: re.sub(r"\d+", "", s).strip()
    assert strip_digits(after[0]) != strip_digits(after[1]), "the main word 'house' was accepted as an answer"


def test_1c_ii_percentage_counts_each_answer_once(sol, monkeypatch, capsys):
    """9618_s24_42:1(c)(i) MP3, MP5 and 9618_s24_42:1(c)(ii) MP1: she twice still counts once -> 7.14 %."""
    _, after = play(sol, monkeypatch, capsys, EASY, ["she", "she", "no"])
    assert has_percentage(after[-1], 100 / 14), "percentage 7.14 (1 of 14) not output after 'no'"
    assert not has_percentage(after[-1], 200 / 14)


def test_1c_ii_outputs_answers_not_entered(sol, monkeypatch, capsys):
    """9618_s24_42:1(c)(ii) MP2-MP3: after the percentage, every answer not entered (and not 'she')."""
    _, after = play(sol, monkeypatch, capsys, EASY, ["she", "out", "no"])
    rest = after_percentage(after[-1].splitlines(), 100 / 14)
    assert rest is not None, "percentage 7.14 not output"
    toks = tokens(rest)
    missing = [w for w in EASY[:13] if w not in toks]
    assert not missing, f"answers not entered are missing from the output: {missing}"
    assert "she" not in toks, "'she' was entered but is listed as missed"


def test_1c_ii_all_found_is_100_percent(sol, monkeypatch, capsys):
    """9618_s24_42:1(c)(ii) MP1: finding every answer gives 100 %."""
    _, after = play(sol, monkeypatch, capsys, ["abc", "bcd"], ["bcd", "abc", "no"])
    assert has_percentage(after[-1], 100.0)


# ---------------------------------------------------------------- 1(b) / 1(d)

def run(candidate_path, exercise_dir, *inputs):
    return run_script(candidate_path, stdin="".join(f"{v}\n" for v in inputs), files_dir=exercise_dir / "files")


@pytest.mark.parametrize("choice,main,count", [("easy", "house", 14), ("medium", "direct", 44), ("hard", "fainted", 97)])
def test_1b_choice_selects_file(candidate_path, exercise_dir, choice, main, count):
    """9618_s24_42:1(b) MP1-MP4 and 9618_s24_42:1(d)(i) MP1: each choice reads its own file and Play() runs."""
    res = run(candidate_path, exercise_dir, choice, "no")
    assert res.returncode == 0, res.stderr[-600:]
    assert main in res.stdout, f"main word {main} not output for {choice}"
    assert count in [int(v) for v in numbers(res.stdout)]


def test_1d_ii_screenshot_easy(candidate_path, exercise_dir):
    """9618_s24_42:1(d)(ii) MP1: easy, she, out, no -> 14 answers, 7.14 %, 13 missed words (MS p.13 example)."""
    res = run(candidate_path, exercise_dir, "easy", "she", "out", "no")
    assert res.returncode == 0, res.stderr[-600:]
    assert "house" in res.stdout
    rest = after_percentage(res.lines, 100 / 14)
    assert rest is not None, "percentage 7.142857... not output"
    toks = tokens(rest)
    assert all(w in toks for w in EASY[:13]) and "she" not in toks


def test_1d_iii_screenshot_hard(candidate_path, exercise_dir):
    """9618_s24_42:1(d)(iii) MP1: hard, fine, fined, idea, no -> 97 answers, 3 found, 3.09 % (MS p.14 example)."""
    res = run(candidate_path, exercise_dir, "hard", "fine", "fined", "idea", "no")
    assert res.returncode == 0, res.stderr[-600:]
    assert "fainted" in res.stdout and 97 in [int(v) for v in numbers(res.stdout)]
    rest = after_percentage(res.lines, 300 / 97)
    assert rest is not None, "percentage 3.0927... not output"
    _, words = answers(exercise_dir, "Hard.txt")
    toks = tokens(rest)
    missed = [w for w in words if w not in ("fine", "fined", "idea")]
    assert all(w in toks for w in missed)
    assert not {"fine", "fined", "idea"} & set(toks)


def test_1b_1di_traced_main(candidate_path, exercise_dir):
    """9618_s24_42:1(b) MP4; 1(d)(i) whole; MS pp.6,12: choice filename and ReadWords -> Play."""
    from testkit import run_script_traced
    for choice, filename in (("easy", "Easy.txt"), ("medium", "Medium.txt"), ("hard", "Hard.txt")):
        r = run_script_traced(candidate_path, stdin=choice + "\nno\n", files_dir=exercise_dir / "files")
        assert r.error is None
        reads, plays = r.called("ReadWords"), r.called("Play")
        assert reads and plays
        assert list(reads[0].args.values()) == [filename]
        assert next(i for i, c in enumerate(r.calls) if c is reads[0]) < next(i for i, c in enumerate(r.calls) if c is plays[0])
        assert answers(exercise_dir, filename)[0] in r.stdout
