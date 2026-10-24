import re
"""w25/43 Q2; MS screenshot 19051306 and QP complete run-length encoding."""
import pytest
from testkit import output_lines, run_script, run_script_traced, use_files


def test_2a_globals(sol):
    """9618_w25_43:2(a) MP1-MP2: 100 empty strings, both pointers -1, count zero."""
    assert sol.Queue == [''] * 100
    assert sol.QueueHead == sol.QueueTail == -1 and sol.NumberItems == 0


def test_2b_last_used_tail_capacity(sol):
    """9618_w25_43:2(b) MP1-MP5: tail is last used, count updated, full returns Boolean False."""
    for i in range(100):
        assert sol.Enqueue(str(i % 2)) is True
        assert sol.QueueTail == i and sol.QueueHead == 0 and sol.NumberItems == i + 1
        assert sol.Queue[i] == str(i % 2)
    before = sol.Queue.copy()
    assert sol.Enqueue('1') is False
    assert sol.Queue == before and sol.QueueTail == 99 and sol.NumberItems == 100


def test_2c_dequeue_string_false_and_fifo(sol):
    """9618_w25_43:2(c) MP1-MP3: string False sentinel, FIFO, move head, decrement count."""
    assert sol.Dequeue() == 'False'
    for value in '1011':
        sol.Enqueue(value)
    for i, value in enumerate('1011'):
        assert sol.Dequeue() == value
        assert sol.QueueHead == i + 1 and sol.NumberItems == 3 - i
    assert sol.Dequeue() == 'False' and sol.NumberItems == 0


def test_2d_reads_official_file(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w25_43:2(d) MP3-MP5: every string digit passed to Enqueue, line endings removed."""
    work = use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    expected = (work / 'BinaryData.txt').read_text().splitlines()
    original = sol.Enqueue
    calls = []

    def spy(value):
        calls.append(value)
        return original(value)

    monkeypatch.setattr(sol, 'Enqueue', spy)
    sol.ReadData()
    assert calls == expected
    assert sol.Queue[:len(expected)] == expected
    assert sol.NumberItems == len(expected)


@pytest.mark.parametrize('length', [0, 1, 17, 100])
def test_2d_any_file_length_to_100(sol, monkeypatch, tmp_path, exercise_dir, length):
    """9618_w25_43:2(d) MP3-MP5: any length <=100, including unterminated last line."""
    work = use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    values = [str(i % 2) for i in range(length)]
    (work / 'BinaryData.txt').write_bytes('\r\n'.join(values).encode('ascii'))
    sol.ReadData()
    assert sol.NumberItems == length and sol.Queue[:length] == values


def test_2d_missing_file(sol, monkeypatch, tmp_path, capsys):
    """9618_w25_43:2(d) MP6: file exception handled with output."""
    monkeypatch.chdir(tmp_path)
    sol.ReadData()
    assert capsys.readouterr().out.strip()


@pytest.mark.parametrize('digits,expected', [('1', '11'), ('0', '01'), ('11000111', '120313'),
                                           ('01', '0111'), ('1010', '11011101'),
                                           ('111111111000000000', '1909'), ('01' * 50, '0111' * 50)])
def test_2e_compress_all_runs_including_final_singleton(sol, monkeypatch, digits, expected):
    """9618_w25_43:2(e) MP1-MP6: calls Dequeue, counts consecutive runs, appends every run."""
    for value in digits:
        sol.Enqueue(value)
    original = sol.Dequeue
    calls = []

    def spy():
        value = original()
        calls.append(value)
        return value

    monkeypatch.setattr(sol, 'Dequeue', spy)
    sol.Compress()
    assert sol.NewString == expected
    assert calls[:len(digits)] == list(digits)
    assert len(digits) <= len(calls) <= len(digits) + 1
    assert sol.NumberItems == 0


def test_2f_ii_screenshot_official_compressed_output(candidate_path, exercise_dir):
    """9618_w25_43:2(f)(i) MP1-MP2; 2(f)(ii) whole: MS p.31 shows 19051306."""
    result = run_script(candidate_path, files_dir=exercise_dir / 'files')
    assert result.returncode == 0, result.stderr
    assert re.search(r'\b19051306\b', result.stdout)


def test_2f_main_call_chain(candidate_path, exercise_dir, tmp_path):
    """9618_w25_43:2(f)(i) MP1-MP2 (MS p.30): ReadData -> Compress -> actual compressed string."""
    for files, expected in [(exercise_dir / 'files', '19051306'), (tmp_path, '120313')]:
        (tmp_path / 'BinaryData.txt').write_text('1\n1\n0\n0\n0\n1\n1\n1')
        completed = run_script(candidate_path, files_dir=files, timeout=5.0)
        assert completed.returncode == 0, completed.stderr
        r = run_script_traced(candidate_path, files_dir=files)
        assert r.error is None, r.error
        names = [c.name for c in r.calls if c.name in ('ReadData', 'Compress')]
        assert names == ['ReadData', 'Compress']
        digits = [c.result for c in r.called('Dequeue') if c.result != 'False']
        assert digits == (files / 'BinaryData.txt').read_text().splitlines()
        assert re.search(r'\b' + expected + r'\b', r.stdout)
