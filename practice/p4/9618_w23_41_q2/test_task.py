"""w23/41 Q2: linear queue, file and records (exact matching MS)."""
import re
from testkit import run_script, run_script_traced, use_files

EXPECTED = [('1234', 1), ('1568', 1), ('9512', 2), ('4567', 4), ('8512', 6),
            ('4125', 3), ('9651', 1), ('4851', 1), ('2520', 2), ('3265', 1), ('8966', 1)]


def record_pair(record):
    ident = record.GetID() if hasattr(record, 'GetID') else record.ID
    total = record.GetTotal() if hasattr(record, 'GetTotal') else record.Total
    return ident, total


def test_2a_i_globals(sol):
    """9618_w23_41:2(a)(i) MP1-MP2; 2(c)(ii) MP1-MP2."""
    assert isinstance(sol.Queue, list) and len(sol.Queue) >= 50
    assert sol.HeadPointer == -1 and sol.TailPointer == 0
    assert isinstance(sol.Records, list) and len(sol.Records) == 50
    assert sol.NumberRecords == 0


def test_2a_ii_enqueue_full(sol, capsys):
    """9618_w23_41:2(a)(ii) MP2-MP4: fills queue; full message and no corruption."""
    for i in range(50):
        sol.Enqueue(str(1000 + i))
        assert sol.Queue[i] == str(1000 + i)
        assert sol.HeadPointer == 0 and sol.TailPointer == i + 1
    before = sol.Queue.copy()
    capsys.readouterr()
    sol.Enqueue('overflow')
    assert capsys.readouterr().out.strip()
    assert sol.Queue == before and sol.TailPointer == 50


def test_2a_iii_dequeue_empty_and_fifo(sol, capsys):
    """9618_w23_41:2(a)(iii) MP2-MP5: empty sentinel, output, FIFO and pointers."""
    assert sol.Dequeue() == 'Empty'
    assert capsys.readouterr().out.strip()
    for value in ['A', 'B', 'C']:
        sol.Enqueue(value)
    assert [sol.Dequeue() for _ in range(3)] == ['A', 'B', 'C']
    capsys.readouterr()
    assert sol.Dequeue() == 'Empty'
    assert capsys.readouterr().out.strip()
    sol.Enqueue('D')
    assert sol.Dequeue() == 'D'


def test_2b_read_official_file(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w23_41:2(b) MP2, MP4-MP6: reads every game ID and calls Enqueue."""
    work = use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    expected = (work / 'QueueData.txt').read_text().splitlines()
    calls = []
    enqueue = sol.Enqueue

    def spy(value):
        calls.append(value)
        return enqueue(value)

    monkeypatch.setattr(sol, 'Enqueue', spy)
    sol.ReadData()
    assert calls == expected
    assert [sol.Dequeue() for _ in expected] == expected


def test_2b_missing_file(sol, monkeypatch, tmp_path, capsys):
    """9618_w23_41:2(b) MP7: missing file is handled with output."""
    monkeypatch.chdir(tmp_path)
    sol.ReadData()
    assert capsys.readouterr().out.strip()


def test_2c_iii_total_first_existing_and_new(sol, monkeypatch):
    """9618_w23_41:2(c)(iii) MP1-MP5: consume one item and update/append exactly once."""
    values = iter(['A', 'B', 'A', 'C', 'B', 'C', 'C'])
    calls = []

    def dequeue():
        value = next(values)
        calls.append(value)
        return value

    monkeypatch.setattr(sol, 'Dequeue', dequeue)
    states = [[('A', 1)], [('A', 1), ('B', 1)], [('A', 2), ('B', 1)],
              [('A', 2), ('B', 1), ('C', 1)], [('A', 2), ('B', 2), ('C', 1)],
              [('A', 2), ('B', 2), ('C', 2)], [('A', 2), ('B', 2), ('C', 3)]]
    for i, expected in enumerate(states):
        sol.TotalData()
        assert len(calls) == i + 1
        assert sol.NumberRecords == len(expected)
        assert [record_pair(r) for r in sol.Records[:sol.NumberRecords]] == expected


def test_2d_output_records(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_w23_41:2(d) whole: ID/Total for all records, in specified format."""
    use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    sol.ReadData()
    for _ in range(23):
        sol.TotalData()
    capsys.readouterr()
    sol.OutputRecords()
    pairs = re.findall(r'ID\s+(\d+)\s+Total\s+(\d+)', capsys.readouterr().out)
    assert [(i, int(n)) for i, n in pairs] == EXPECTED


def test_2e_ii_screenshot_totals(candidate_path, exercise_dir):
    """9618_w23_41:2(e)(i) MP1-MP2; 2(e)(ii) whole: MS p.24 screenshot."""
    result = run_script(candidate_path, files_dir=exercise_dir / 'files')
    assert result.returncode == 0, result.stderr
    pairs = re.findall(r'ID\s+(\d+)\s+Total\s+(\d+)', result.stdout)
    assert [(i, int(n)) for i, n in pairs] == EXPECTED


def assert_numbers_in_order(text, expected):
    """D31/D46: allow explanatory numbers and line breaks around required values."""
    values = iter(float(n) for n in re.findall(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])", text))
    for wanted in expected:
        assert any(value == wanted for value in values), f"missing ordered value {wanted}: {text!r}"


def test_2e_main_call_chain(candidate_path, exercise_dir):
    """9618_w23_41:2(e)(i) MP1-MP2 (QP p.7/MS p.23): ReadData first, each TotalData, OutputRecords last."""
    data = ''
    completed = run_script(candidate_path, stdin=data, files_dir=exercise_dir / 'files', timeout=1.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data, files_dir=exercise_dir / 'files')
    assert r.error is None, r.error
    names = [c.name for c in r.calls if c.name in ('ReadData', 'TotalData', 'OutputRecords')]
    assert names == ['ReadData'] + ['TotalData'] * 23 + ['OutputRecords']
    data = (exercise_dir / 'files/QueueData.txt').read_text().splitlines()
    assert [c.result for c in r.called('Dequeue')] == data
    pairs = re.findall(r'ID\s+(\d+)\s+Total\s+(\d+)', r.stdout)
    assert [(i, int(n)) for i, n in pairs] == EXPECTED

