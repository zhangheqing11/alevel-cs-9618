"""9618_s22_42 Q1 stack; MS accepts uncleared or cleared popped slots."""
import re
from testkit import run_script, run_script_traced


def nums(text):
    return [int(x) for x in re.findall(r'-?\d+', text)]


def test_1a_declarations(sol):
    """9618_s22_42:1(a) MP1-MP3: array and next-free pointer."""
    assert isinstance(sol.StackData, list) and len(sol.StackData) == 10
    assert sol.StackPointer == 0


def test_1b_printarray(sol, capsys):
    """9618_s22_42:1(b) MP2-MP3 (MS p.5): all cells and pointer; no QP output order constraint."""
    sol.StackData = list(range(11, 21)); sol.StackPointer = 4
    sol.PrintArray()
    text = capsys.readouterr().out
    assert_numbers_in_order(text, list(range(11, 21)))
    assert 4 in nums(text)


def test_1c_push_boundary(sol):
    """9618_s22_42:1(c) MP2-MP6: ten additions, full rejects without changing data."""
    for i in range(10):
        assert sol.Push(11 + i) is True
        assert sol.StackPointer == i + 1 and sol.StackData[i] == 11 + i
    before = sol.StackData[:]
    assert sol.Push(21) is False
    assert sol.StackPointer == 10 and sol.StackData == before


def test_1e_pop_lifo_empty_reuse(sol):
    """9618_s22_42:1(e)(i) MP1-MP5: numeric return, LIFO, empty sentinel, slot reuse."""
    assert sol.Pop() == -1 and sol.StackPointer == 0
    for v in [3, 7, 0, -6]:
        sol.Push(v)
    for remaining, expected in [(3, -6), (2, 0), (1, 7), (0, 3)]:
        assert sol.Pop() == expected and sol.StackPointer == remaining
    assert sol.Pop() == -1
    assert sol.Push(42) is True and sol.Pop() == 42


def test_1d_screenshot(candidate_path):
    """9618_s22_42:1(d)(ii) whole (MS p.10): stored array, allow explanatory digits."""
    r = run_script(candidate_path, stdin='\n'.join(map(str, range(11, 22))) + '\n')
    assert r.returncode == 0, r.stderr
    assert_numbers_in_order(r.stdout, list(range(11, 21)))


def test_1e_screenshot_after_two_pops(candidate_path):
    """9618_s22_42:1(e)(ii) MP1-MP2 (MS p.12): accept all three MS slot variants."""
    r = run_script(candidate_path, stdin='\n'.join(map(str, range(11, 22))) + '\n')
    assert r.returncode == 0, r.stderr
    assert_numbers_in_order(r.stdout, list(range(11, 21)) + list(range(11, 19)))


def test_1b_no_algorithm_shortcuts(candidate_path):
    """9618_s22_42:1(c) MP2 (D10): required algorithm cannot be delegated to built-ins."""
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


def test_1d_1e_main_call_chain(candidate_path):
    """9618_s22_42:1(d)(i) MP1-MP5;1(e)(ii) MP1-MP2 (MS pp.8/12): main uses stack operations."""
    data = '11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n'
    completed = run_script(candidate_path, stdin=data, timeout=5.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data)
    assert r.error is None, r.error
    pushes = r.called('Push')
    assert [next(iter(c.args.values())) for c in pushes] == list(range(11, 22))
    assert [c.result for c in pushes] == [True] * 10 + [False]
    assert [c.name for c in r.calls if c.name in ('Push', 'PrintArray', 'Pop')] == ['Push'] * 11 + ['PrintArray', 'Pop', 'Pop', 'PrintArray']
    assert [c.result for c in r.called('Pop')] == [20, 19]
    assert_numbers_in_order(r.stdout, list(range(11, 21)) + list(range(11, 19)))

