"""w24/42 Q2: queue record; supports scalar and MS (record, value) returns."""
import inspect
import json
import re
from testkit import output_lines, run_script


def field(q, name):
    spelling = name if hasattr(q, name) else name.replace('Pointer', 'pointer')
    return getattr(q, spelling)


def put(q, name, value):
    spelling = name if hasattr(q, name) else name.replace('Pointer', 'pointer')
    setattr(q, spelling, value)


def fresh(sol):
    q = sol.Queue()
    q.QueueArray = [-1] * 100
    put(q, 'HeadPointer', -1)
    put(q, 'TailPointer', 0)
    sol.TheQueue = q
    return q


def call(sol, name, q, *args):
    sol.TheQueue = q
    fn = getattr(sol, name)
    count = len(inspect.signature(fn).parameters)
    result = fn(q, *args) if count == len(args) + 1 else fn(*args)
    if isinstance(result, tuple):
        assert len(result) == 2
        return result
    return q, result


def run_traced(candidate_path, tmp_path, stdin):
    """Record initial queue at first Enqueue; do not prescribe where it was initialised."""
    record = tmp_path / 'first_enqueue.json'
    wrapper = tmp_path / 'trace_main.py'
    wrapper.write_text(
        'import json, runpy, sys\n'
        f'target = {str(candidate_path)!r}\n'
        'states = []\n'
        'def trace(frame, event, arg):\n'
        '    if event == "call" and frame.f_code.co_name == "Enqueue":\n'
        '        candidates = list(frame.f_locals.values()) + list(frame.f_globals.values())\n'
        '        for q in candidates:\n'
        '            if not isinstance(q, type) and hasattr(q, "QueueArray"):\n'
        '                hp = getattr(q, "HeadPointer", getattr(q, "Headpointer", None))\n'
        '                tp = getattr(q, "TailPointer", getattr(q, "Tailpointer", None))\n'
        '                states.append([hp, tp, list(q.QueueArray)])\n'
        '                break\n'
        '    return trace\n'
        'sys.settrace(trace)\n'
        'try:\n'
        '    runpy.run_path(target, run_name="__main__")\n'
        'finally:\n'
        '    sys.settrace(None)\n'
        f'    open({str(record)!r}, "w").write(json.dumps(states))\n'
    )
    result = run_script(wrapper, stdin=stdin)
    return result, json.loads(record.read_text())


def test_2a_record_array(sol):
    """9618_w24_42:2(a) MP2: Queue has a real 100-element list (types manual)."""
    q = sol.Queue()
    assert isinstance(q.QueueArray, list) and len(q.QueueArray) == 100


def test_2b_record_initialised_before_enqueue(candidate_path, tmp_path):
    """9618_w24_42:2(b) MP1-MP3: first enqueue sees -1/0 and 100 values -1."""
    result, states = run_traced(candidate_path, tmp_path, '\n'.join(map(str, range(10))) + '\n')
    assert result.returncode == 0, result.stderr
    assert len(states) == 10
    assert states[0] == [-1, 0, [-1] * 100]


def test_2c_enqueue_first_and_capacity(sol):
    """9618_w24_42:2(c) MP1-MP2: three completed statements; +/-1 status and pointers."""
    q = fresh(sol)
    for i in range(100):
        q, status = call(sol, 'Enqueue', q, i + 1)
        assert status == 1
        assert field(q, 'HeadPointer') == 0 and field(q, 'TailPointer') == i + 1
        assert q.QueueArray[i] == i + 1
    before = q.QueueArray.copy()
    q, status = call(sol, 'Enqueue', q, 999)
    assert status == -1 and q.QueueArray == before and field(q, 'TailPointer') == 100


def test_2d_all_data_without_removing(sol):
    """9618_w24_42:2(d) MP1-MP3: HeadPointer through TailPointer-1, spaced string."""
    q = fresh(sol)
    q.QueueArray[0:5] = [99, 77, 13, 0, 42]
    put(q, 'HeadPointer', 2)
    put(q, 'TailPointer', 5)
    before = q.QueueArray.copy()
    _, result = call(sol, 'ReturnAllData', q)
    assert isinstance(result, str) and result.split() == ['13', '0', '42']
    assert q.QueueArray == before and field(q, 'HeadPointer') == 2 and field(q, 'TailPointer') == 5


def test_2f_dequeue_fifo_preserves_cells(sol):
    """9618_w24_42:2(f) MP1-MP4: -1 when empty, return head and move pointer only."""
    q = fresh(sol)
    q, value = call(sol, 'Dequeue', q)
    assert value == -1
    for value in [0, 7, 19]:
        q, _ = call(sol, 'Enqueue', q, value)
    before = q.QueueArray.copy()
    for i, expected in enumerate([0, 7, 19]):
        q, value = call(sol, 'Dequeue', q)
        assert value == expected and field(q, 'HeadPointer') == i + 1
        assert q.QueueArray == before
    q, value = call(sol, 'Dequeue', q)
    assert value == -1


def test_2e_ii_screenshot_rejects_negative(candidate_path, tmp_path):
    """9618_w24_42:2(e)(i) MP1-MP5; 2(e)(ii) MP1-MP2: ten valid inputs."""
    result, states = run_traced(candidate_path, tmp_path, '10\n9\n-1\n8\n7\n6\n5\n4\n3\n2\n1\n')
    assert result.returncode == 0, result.stderr
    assert len(states) == 10
    assert states[-1][2][:9] == [10, 9, 8, 7, 6, 5, 4, 3, 2]
    assert any(line.strip() == '10 9 8 7 6 5 4 3 2 1' for line in output_lines(result.stdout))
    # Messages may include the input prompt on the same line, and need not say 'Inserted'.
    assert len(output_lines(result.stdout)) >= 13


def test_2e_i_zero_is_valid(candidate_path):
    """9618_w24_42:2(e)(i) MP3: zero is accepted, negative input retried."""
    result = run_script(candidate_path, stdin='-5\n' + '\n'.join(map(str, range(10))) + '\n')
    assert result.returncode == 0, result.stderr
    assert any(line.strip() == '0 1 2 3 4 5 6 7 8 9' for line in output_lines(result.stdout))


def test_2g_ii_screenshot_two_returns(candidate_path):
    """9618_w24_42:2(g)(i) MP1-MP3; 2(g)(ii) whole: returns 10 then 9."""
    result = run_script(candidate_path, stdin='10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n')
    assert result.returncode == 0, result.stderr
    lines = output_lines(result.stdout)
    start = next(i for i, line in enumerate(lines) if line.strip() == '10 9 8 7 6 5 4 3 2 1')
    assert re.findall(r'-?\d+', lines[start + 1]) == ['10']
    assert re.findall(r'-?\d+', lines[start + 2]) == ['9']
    assert lines[-1].strip() == '8 7 6 5 4 3 2 1'
