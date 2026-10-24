import re
"""Circular queue tests derived from the matching 9618_s22_41 MS."""
from testkit import output_lines, run_script, run_script_traced


def test_3a_initial_state(sol):
    """9618_s22_41:3(a) MP1-MP2: ten strings, all pointers/count initially zero."""
    assert isinstance(sol.QueueArray, list) and len(sol.QueueArray) == 10
    assert (sol.QueueHeadPointer, sol.QueueTailPointer, sol.NumberOfItems) == (0, 0, 0)


def test_3b_enqueue_full_and_wrap(sol):
    """9618_s22_41:3(b) MP1: complete five missing statements, preserving ByRef state."""
    queue = [''] * 10
    head = tail = count = 0
    for i in range(10):
        ok, queue, head, tail, count = sol.Enqueue(queue, head, tail, count, str(i))
        assert ok is True and queue[i] == str(i)
        assert (head, tail, count) == (0, (i + 1) % 10, i + 1)
    before = queue[:]
    ok, queue, head, tail, count = sol.Enqueue(queue, head, tail, count, 'overflow')
    assert ok is False and queue == before and (head, tail, count) == (0, 0, 10)


def test_3c_dequeue_fifo_empty_and_wrap(sol):
    """9618_s22_41:3(c) MP2-MP7: empty return; FIFO, decrement, wrap after index 9."""
    queue = [str(i) for i in range(10)]
    head, tail, count = 0, 0, 10
    for i in range(10):
        value, queue, head, tail, count = sol.Dequeue(queue, head, tail, count)
        assert value == str(i)
        assert (head, tail, count) == ((i + 1) % 10, 0, 9 - i)
    value, queue, head, tail, count = sol.Dequeue(queue, head, tail, count)
    assert value == 'FALSE' and (head, tail, count) == (0, 0, 0)


def test_3bc_reuse_slots_after_dequeue(sol):
    """9618_s22_41:3(b) MP1; 3(c) MP4-MP7: repeated enqueue/dequeue crossing both boundaries."""
    q = [''] * 10
    h = t = n = 0
    for cycle in range(3):
        for i in range(10):
            ok, q, h, t, n = sol.Enqueue(q, h, t, n, f'{cycle}:{i}')
            assert ok is True
        for i in range(10):
            v, q, h, t, n = sol.Dequeue(q, h, t, n)
            assert v == f'{cycle}:{i}'
        assert n == 0


def test_3d_screenshot(candidate_path):
    """9618_s22_41:3(d)(ii) whole (MS p.34): A, B in order; messages reviewed separately."""
    r = run_script(candidate_path, stdin='\n'.join('ABCDEFGHIJK') + '\n')
    assert r.returncode == 0, r.stderr
    assert re.search(r'\bA\b[\s\S]*\bB\b', r.stdout)




def test_3b_no_algorithm_shortcuts(candidate_path):
    """9618_s22_41:3(b) MP1 (D10): required algorithm cannot be delegated to built-ins."""
    import ast
    tree = ast.parse(candidate_path.read_text(encoding='utf-8'))
    forbidden = {'sort', 'sorted', 'index', 'count', 'max', 'min'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else '')
            assert name not in forbidden, f'D10: implement the algorithm without {name}()'
        if isinstance(node, ast.Compare):
            assert not any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops), \
                'D10: implement search with pointers/comparisons rather than membership'


def assert_numbers_in_order(text, expected):
    """D31/D46: allow explanatory numbers and line breaks around required values."""
    values = iter(float(n) for n in re.findall(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])", text))
    for wanted in expected:
        assert any(value == wanted for value in values), f"missing ordered value {wanted}: {text!r}"


def test_3d_main_call_chain(candidate_path):
    """9618_s22_41:3(d)(i) MP1-MP5 (MS p.32): 11 inputs passed, two returned values output."""
    data = 'A\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\n'
    completed = run_script(candidate_path, stdin=data, timeout=1.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data)
    assert r.error is None, r.error
    enqueues, dequeues = r.called('Enqueue'), r.called('Dequeue')
    assert [c.args.get('InputData') for c in enqueues] == list('ABCDEFGHIJK')
    assert [c.result[0] for c in enqueues] == [True] * 10 + [False]
    assert len(dequeues) == 2 and [c.result[0] for c in dequeues] == ['A', 'B']
    assert r.calls.index(enqueues[-1]) < r.calls.index(dequeues[0])
    assert re.search(r'\bA\b[\s\S]*\bB\b', r.stdout)



def assert_numbers_in_order(text, expected):
    """D31/D46: allow explanatory numbers and line breaks around required values."""
    values = iter(float(n) for n in re.findall(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])", text))
    for wanted in expected:
        assert any(value == wanted for value in values), f"missing ordered value {wanted}: {text!r}"


def test_3d_main_call_chain(candidate_path):
    """9618_s22_41:3(d)(i) MP1-MP5 (MS p.32): 11 inputs passed, two returned values output."""
    data = 'A\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\n'
    completed = run_script(candidate_path, stdin=data, timeout=1.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data)
    assert r.error is None, r.error
    enqueues, dequeues = r.called('Enqueue'), r.called('Dequeue')
    assert [c.args.get('InputData') for c in enqueues] == list('ABCDEFGHIJK')
    assert [c.result[0] for c in enqueues] == [True] * 10 + [False]
    assert len(dequeues) == 2 and [c.result[0] for c in dequeues] == ['A', 'B']
    assert r.calls.index(enqueues[-1]) < r.calls.index(dequeues[0])
    assert re.search(r'\bA\b[\s\S]*\bB\b', r.stdout)

