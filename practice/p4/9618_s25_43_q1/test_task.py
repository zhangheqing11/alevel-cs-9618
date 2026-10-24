"""9618_s25_43 Q1 linear queue and dequeue-based total."""
from pathlib import Path
import re
from testkit import run_script, use_files


def test_1a_initial_state(sol):
    """9618_s25_43:1(a) MP1-MP3: fifty integer -1s and both pointers -1."""
    assert isinstance(sol.Queue, list) and sol.Queue == [-1] * 50
    assert (sol.HeadPointer, sol.TailPointer) == (-1, -1)


def test_1b_enqueue_full(sol):
    """9618_s25_43:1(b) MP2-MP6: first head, last tail, capacity, noncircular full case."""
    for i in range(50):
        assert sol.Enqueue(i + 1) is True
        assert sol.Queue[i] == i + 1
        assert (sol.HeadPointer, sol.TailPointer) == (0, i)
    before = sol.Queue[:]
    assert sol.Enqueue(51) is False and sol.Queue == before
    sol.Dequeue()
    assert sol.Enqueue(52) is False


def test_1c_dequeue_fifo_empty(sol):
    """9618_s25_43:1(c) MP1-MP5: sentinel -1, return head before incrementing."""
    assert sol.Dequeue() == -1
    for i in [19, 8, 62]:
        sol.Enqueue(i)
    for i, expected in enumerate([19, 8, 62]):
        assert sol.Dequeue() == expected and sol.HeadPointer == i + 1
    assert sol.Dequeue() == -1


def test_1d_official_file(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_s25_43:1(d) MP2-MP4: integer conversion and Enqueue of all official lines."""
    use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    expected = [int(x) for x in Path('QueueData.txt').read_text().splitlines()]
    calls = []; original = sol.Enqueue
    def spy(value):
        calls.append(value); return original(value)
    monkeypatch.setattr(sol, 'Enqueue', spy)
    sol.CreateQueue()
    assert calls == expected
    assert sol.Queue[:len(expected)] == expected
    assert (sol.HeadPointer, sol.TailPointer) == (0, len(expected) - 1)


def test_1d_unknown_length_overflow_and_missing(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s25_43:1(d) MP2/MP5/MP6: 53 lines, full message once or repeatedly, missing file."""
    use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    Path('QueueData.txt').write_text('\n'.join(map(str, range(1, 54))))
    sol.CreateQueue()
    assert sol.Queue == list(range(1, 51)) and sol.TailPointer == 49
    assert 'Queue full' in capsys.readouterr().out
    Path('QueueData.txt').unlink()
    sol.CreateQueue()
    assert capsys.readouterr().out.strip()


def test_1e_screenshot(candidate_path, exercise_dir):
    """9618_s25_43:1(e)(i) MP1-MP5; 1(e)(ii) whole: own MS p.18 total 3059."""
    r = run_script(candidate_path, files_dir=exercise_dir / 'files')
    assert r.returncode == 0, r.stderr
    assert re.findall(r'-?\d+', r.stdout)[-1] == '3059'


def test_1e_main_uses_dequeue_until_sentinel(candidate_path, tmp_path, exercise_dir):
    """9618_s25_43:1(e)(i) MP2-MP4: sum must use repeated Dequeue, excluding sentinel."""
    wrapper = tmp_path / 'observe_queue.py'
    wrapper.write_text(
        'import runpy, sys\n'
        'calls = []\n'
        'def trace(frame, event, arg):\n'
        "    if event == 'return' and frame.f_code.co_name == 'Dequeue':\n"
        '        calls.append(arg)\n'
        '    return trace\n'
        'sys.settrace(trace)\n'
        f"runpy.run_path({str(candidate_path)!r}, run_name='__main__')\n"
        'sys.settrace(None)\n'
        'assert calls and calls[-1] == -1\n'
        'assert sum(calls[:-1]) == 3059\n'
    )
    r = run_script(wrapper, files_dir=exercise_dir / 'files')
    assert r.returncode == 0, r.stderr
