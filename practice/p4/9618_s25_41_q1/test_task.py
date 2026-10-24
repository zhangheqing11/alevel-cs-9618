"""9618_s25_41 Q1 circular queue; tail means last stored item."""
import re
from testkit import output_lines, run_script, run_script_traced


def test_1a_initial_state(sol):
    """9618_s25_41:1(a) MP1-MP2: twenty -1 entries, pointers -1, count zero."""
    assert isinstance(sol.Queue, list) and sol.Queue == [-1] * 20
    assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (-1, -1, 0)


def test_1b_enqueue_full(sol):
    """9618_s25_41:1(b) MP1-MP6: first insertion, pointer and count, full failure."""
    for i in range(20):
        assert sol.Enqueue(i + 1) is True
        assert sol.Queue[i] == i + 1
        assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (0, i, i + 1)
    before = sol.Queue[:]
    assert sol.Enqueue(21) is False and sol.Queue == before
    assert sol.NumberItems == 20


def test_1bd_wrap_partial_dequeue_and_refill(sol):
    """9618_s25_41:1(b) MP4-MP6; 1(d) MP2-MP5: wrap while queue remains nonempty."""
    for i in range(1, 21):
        sol.Enqueue(i)
    for i in range(1, 8):
        assert sol.Dequeue() == i
    for i in range(21, 28):
        assert sol.Enqueue(i) is True
    assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (7, 6, 20)
    for i in range(8, 28):
        assert sol.Dequeue() == i
    assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (-1, -1, 0)


def test_1d_empty_reset_and_reuse(sol):
    """9618_s25_41:1(d) MP1/MP5/MP6: last deletion resets both pointers, next insert works."""
    assert sol.Dequeue() == -1
    for i in range(3):
        assert sol.Enqueue(i + 1) is True and sol.Dequeue() == i + 1
        assert (sol.HeadPointer, sol.TailPointer, sol.NumberItems) == (-1, -1, 0)
        assert sol.Dequeue() == -1


def test_1ce_screenshot(candidate_path):
    """9618_s25_41:1(c) MP3;1(e)(ii) whole (QP p.3/MS pp.12/16): status with integer, line breaks allowed."""
    r = run_script(candidate_path)
    assert r.returncode == 0, r.stderr
    pairs = re.findall(r'\b(\d+)\s+(Successful|Unsuccessful)\b', r.stdout)
    assert [(int(n), status) for n, status in pairs] == [(i, 'Successful' if i <= 20 else 'Unsuccessful') for i in range(1, 26)]
    assert_numbers_in_order(r.stdout[r.stdout.rfind('Unsuccessful') + len('Unsuccessful'):], [1, 2])



def test_1b_no_algorithm_shortcuts(candidate_path):
    """9618_s25_41:1(b) MP1 (D10): required algorithm cannot be delegated to built-ins."""
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


def test_1c_1e_main_call_chain(candidate_path):
    """9618_s25_41:1(c) MP1-MP3;1(e)(i) MP1-MP2 (MS pp.12/16): 25 enqueues then two dequeues."""
    data = ''
    completed = run_script(candidate_path, stdin=data, timeout=1.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data)
    assert r.error is None, r.error
    enqueues, dequeues = r.called('Enqueue'), r.called('Dequeue')
    assert [next(iter(c.args.values())) for c in enqueues] == list(range(1, 26))
    assert [c.result for c in enqueues] == [True] * 20 + [False] * 5
    assert [c.result for c in dequeues] == [1, 2]
    assert r.calls.index(enqueues[-1]) < r.calls.index(dequeues[0])
    assert_numbers_in_order(r.stdout[r.stdout.rfind('Unsuccessful') + len('Unsuccessful'):], [c.result for c in dequeues])

