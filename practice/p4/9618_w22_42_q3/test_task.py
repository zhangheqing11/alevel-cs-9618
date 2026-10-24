"""Exact matching w22/42 Q3 MS; corpus MP numbering."""
import re

from testkit import run_script, run_script_traced


def test_3a_queue_and_pointers(sol):
    """9618_w22_42:3(a) MP1-MP3: fixed queue and QP pointer convention."""
    assert isinstance(sol.Queue, list) and len(sol.Queue) == 100
    assert sol.HeadPointer == -1 and sol.TailPointer == 0


def test_3b_first_last_and_full(sol):
    """9618_w22_42:3(b) MP2-MP6: writes before advancing; full failure preserves state."""
    for value in range(100):
        assert sol.Enqueue(value + 12) is True
        assert sol.Queue[value] == value + 12
        assert sol.TailPointer == value + 1 and sol.HeadPointer == 0
    before = sol.Queue.copy()
    assert sol.Enqueue(999) is False
    assert sol.Queue == before and sol.TailPointer == 100


def test_3d_recursive_sum(sol, monkeypatch):
    """9618_w22_42:3(d) MP2-MP6: recursive accumulation to start, pointer decreases."""
    sol.Queue = [8, -3, 17, 0, 9] + [12345] * 95
    sol.HeadPointer = 0
    calls = []
    original = sol.RecursiveOutput

    def spy(start):
        calls.append(start)
        return original(start)

    monkeypatch.setattr(sol, 'RecursiveOutput', spy)
    assert spy(0) == 8
    calls.clear()
    assert spy(4) == 31
    assert calls == [4, 3, 2, 1, 0]


def test_3e_ii_screenshot_total(candidate_path, exercise_dir):
    """9618_w22_42:3(c) MP1-MP4; 3(e)(i) whole; 3(e)(ii) whole: 210."""
    result = run_script(candidate_path, files_dir=exercise_dir / 'files')
    assert result.returncode == 0, result.stderr
    assert 'Successful' in result.stdout and 'Unsuccessful' not in result.stdout
    assert_numbers_in_order(result.stdout, [210])


def test_3c_reports_any_enqueue_failure(candidate_path, tmp_path):
    """9618_w22_42:3(c) MP1-MP4: one failed insertion means Unsuccessful, even if last succeeds."""
    record = tmp_path / 'calls.json'
    wrapper = tmp_path / 'one_failure.py'
    wrapper.write_text(
        'import json, runpy, sys\n'
        'calls = []\n'
        'def trace(frame, event, arg):\n'
        '    if event == "line" and frame.f_globals.get("__name__") == "__main__":\n'
        '        namespace = frame.f_globals\n'
        '        if "Enqueue" in namespace and "RecursiveOutput" in namespace:\n'
        '            original = namespace["Enqueue"]\n'
        '            def enqueue(value):\n'
        '                calls.append(value)\n'
        '                return False if value == 5 else original(value)\n'
        '            namespace["Enqueue"] = enqueue\n'
        '            sys.settrace(None)\n'
        '            return None\n'
        '    return trace\n'
        'sys.settrace(trace)\n'
        'try:\n'
        f'    runpy.run_path({str(candidate_path)!r}, run_name="__main__")\n'
        'finally:\n'
        '    sys.settrace(None)\n'
        f'    open({str(record)!r}, "w").write(json.dumps(calls))\n'
    )
    result = run_script(wrapper)
    assert result.returncode == 0, result.stderr
    assert 'Unsuccessful' in result.stdout
    import json
    assert json.loads(record.read_text()) == list(range(1, 21))


def assert_numbers_in_order(text, expected):
    """D31/D46: allow explanatory numbers and line breaks around required values."""
    values = iter(float(n) for n in re.findall(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])", text))
    for wanted in expected:
        assert any(value == wanted for value in values), f"missing ordered value {wanted}: {text!r}"


def test_3c_3e_main_call_chain(candidate_path):
    """9618_w22_42:3(c) MP1-MP4;3(e)(i) whole (MS pp.22–23): ordered enqueues and recursive return output."""
    data = ''
    completed = run_script(candidate_path, stdin=data, timeout=1.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data)
    assert r.error is None, r.error
    enqueues, sums = r.called('Enqueue'), r.called('RecursiveOutput')
    assert [next(iter(c.args.values())) for c in enqueues] == list(range(1, 21))
    assert sums and sums[0].args.get('Start') == 19 and sums[0].result == 210
    assert r.calls.index(enqueues[-1]) < r.calls.index(sums[0])
    assert_numbers_in_order(r.stdout, [sums[0].result])

