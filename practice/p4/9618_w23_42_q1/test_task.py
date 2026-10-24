"""w23/42 Q1: two stacks; MS output utxoe."""
from testkit import output_lines, run_script, use_files


def test_1a_arrays_and_next_free_pointers(sol):
    """9618_w23_42:1(a)(i) MP1-MP2; 1(a)(ii) whole."""
    assert isinstance(sol.StackVowel, list) and len(sol.StackVowel) == 100
    assert isinstance(sol.StackConsonant, list) and len(sol.StackConsonant) == 100
    assert sol.StackVowel is not sol.StackConsonant
    assert sol.VowelTop == sol.ConsonantTop == 0


def test_1b_i_both_stacks_classify_and_overflow(sol, capsys):
    """9618_w23_42:1(b)(i) MP2-MP6: vowels/consonants, 100th push, full message."""
    vowels = 'aeiou' * 20
    consonants = 'bcdfg' * 20
    for i in range(100):
        sol.PushData(vowels[i])
        sol.PushData(consonants[i])
        assert sol.VowelTop == sol.ConsonantTop == i + 1
        assert sol.StackVowel[i] == vowels[i] and sol.StackConsonant[i] == consonants[i]
    for letter in ['a', 'b']:
        capsys.readouterr()
        sol.PushData(letter)
        assert capsys.readouterr().out.strip()
    assert sol.VowelTop == sol.ConsonantTop == 100
    assert len(sol.StackVowel) == len(sol.StackConsonant) == 100


def test_1b_ii_read_official_letters(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w23_42:1(b)(ii) MP2-MP5: exact source file and calls to PushData."""
    work = use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    expected = (work / 'StackData.txt').read_text().splitlines()
    calls = []
    original = sol.PushData

    def spy(letter):
        calls.append(letter)
        original(letter)

    monkeypatch.setattr(sol, 'PushData', spy)
    sol.ReadData()
    assert calls == expected
    assert sol.StackVowel[:sol.VowelTop] == [s for s in expected if s in 'aeiou']
    assert sol.StackConsonant[:sol.ConsonantTop] == [s for s in expected if s not in 'aeiou']


def test_1b_ii_missing_file(sol, monkeypatch, tmp_path, capsys):
    """9618_w23_42:1(b)(ii) MP6: missing file handled with message."""
    monkeypatch.chdir(tmp_path)
    sol.ReadData()
    assert capsys.readouterr().out.strip()


def test_1c_pop_lifo_empty_and_reuse(sol):
    """9618_w23_42:1(c) MP2-MP5: both stacks LIFO, empty sentinel and next-free pointer."""
    assert sol.PopVowel() == sol.PopConsonant() == 'No data'
    assert sol.VowelTop == sol.ConsonantTop == 0
    for letter in 'abecidofug':
        sol.PushData(letter)
    assert [sol.PopVowel() for _ in range(5)] == list('uoiea')
    assert [sol.PopConsonant() for _ in range(5)] == list('gfdcb')
    assert sol.PopVowel() == sol.PopConsonant() == 'No data'
    sol.PushData('e')
    sol.PushData('z')
    assert sol.PopVowel() == 'e' and sol.PopConsonant() == 'z'


def test_1d_ii_screenshot_utxoe(candidate_path, exercise_dir):
    """9618_w23_42:1(d)(i) MP1-MP5, MP7; 1(d)(ii) whole: utxoe."""
    result = run_script(candidate_path, stdin='vowel\nconsonant\nconsonant\nvowel\nvowel\n',
                        files_dir=exercise_dir / 'files')
    assert result.returncode == 0, result.stderr
    assert output_lines(result.stdout)[-1].rstrip().endswith('utxoe')


def test_1d_i_empty_choice_does_not_count_as_letter(candidate_path, tmp_path):
    """9618_w23_42:1(d)(i) MP2, MP6-MP7: retry an empty stack until five successes."""
    for letter, empty_choice, good_choice in [('a', 'consonant', 'vowel'), ('b', 'vowel', 'consonant')]:
        (tmp_path / 'StackData.txt').write_text((letter + '\n') * 100)
        result = run_script(candidate_path, stdin=empty_choice + '\n' + (good_choice + '\n') * 5,
                            files_dir=tmp_path)
        assert result.returncode == 0, result.stderr
        lines = output_lines(result.stdout)
        assert lines[-1].rstrip().endswith(letter * 5)
        # QP requires a message for the failed pop; its wording is not prescribed.
        assert len(lines) >= 2
