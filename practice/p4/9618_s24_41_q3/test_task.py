"""9618_s24_41 Q3 linear queue and weighted check digit."""
import re
from testkit import feed_input, output_lines, run_script, run_script_traced

DATA = ['999999X', '1251484', '5500212', '0033585', '9845788', '6666666', '3258746', '8111022', '7568557', '0012353']


def test_3a_initial_state(sol):
    """9618_s24_41:3(a) whole: twenty nulls and both pointers -1."""
    assert isinstance(sol.QueueData, list) and len(sol.QueueData) == 20
    assert all(x in ('', None) for x in sol.QueueData)
    assert (sol.QueueHead, sol.QueueTail) == (-1, -1)


def test_3b_enqueue_linear_full(sol):
    """9618_s24_41:3(b) MP1-MP4: real array indexing, first head=0, tail=19 is full."""
    for i in range(20):
        assert sol.Enqueue(f'{i:06d}') is True
        assert sol.QueueData[i] == f'{i:06d}'
        assert (sol.QueueHead, sol.QueueTail) == (0, i)
    before = sol.QueueData[:]
    assert sol.Enqueue('999999') is False and sol.QueueData == before
    assert len(sol.QueueData) == 20


def test_3c_dequeue_fifo_and_empty_string(sol):
    """9618_s24_41:3(c) MP1-MP3: string sentinel, FIFO, increment head; no circular reuse."""
    assert sol.Dequeue() == 'false'
    for i in range(20):
        sol.Enqueue(f'{i:06d}')
    for i in range(20):
        assert sol.Dequeue() == f'{i:06d}'
        assert sol.QueueHead == i + 1
    assert sol.Dequeue() == 'false'
    assert sol.Enqueue('999999') is False


def test_3d_storeitems_official_sequence(sol, monkeypatch, capsys):
    """9618_s24_41:3(d)(i) MP1-MP8 max6: ten inputs, six valid, strip digit, four invalid."""
    calls = []
    original = sol.Enqueue
    def spy(value):
        calls.append(value); return original(value)
    monkeypatch.setattr(sol, 'Enqueue', spy)
    feed_input(monkeypatch, *DATA)
    sol.StoreItems()
    assert calls == ['999999', '125148', '550021', '984578', '811102', '756855']
    assert sol.QueueData[:6] == calls
    assert (sol.QueueHead, sol.QueueTail) == (0, 5)
    assert_numbers_in_order(capsys.readouterr().out, [4])


def test_3d_x_and_numeric_checks_at_full_queue(sol, monkeypatch, capsys):
    """9618_s24_41:3(d)(i) MP4-MP8: wrong X rejected; valid X accepted even when full."""
    sol.QueueTail = 19; sol.QueueHead = 0
    feed_input(monkeypatch, *(['954123X', '999999X'] * 5))
    sol.StoreItems()
    out = output_lines(capsys.readouterr().out)
    assert_numbers_in_order('\n'.join(out), [5])
    assert sol.QueueTail == 19


def test_3d_screenshot(candidate_path):
    """9618_s24_41:3(d)(ii) whole; 3(d)(iii) MP1-MP2: four invalid, item code 999999."""
    r = run_script(candidate_path, stdin='\n'.join(DATA) + '\n')
    assert r.returncode == 0, r.stderr
    lines = output_lines(r.stdout)
    assert_numbers_in_order(r.stdout, [4, 999999])


def test_3d_main_empty_message(candidate_path):
    """9618_s24_41:3(d)(ii) whole: suitable message after all ten inputs are invalid."""
    r = run_script(candidate_path, stdin=('9541235\n' * 10))
    assert r.returncode == 0, r.stderr
    lines = output_lines(r.stdout)
    assert_numbers_in_order(r.stdout, [10])
    assert r.stdout.strip() and '954123' not in r.stdout


def test_3b_no_algorithm_shortcuts(candidate_path):
    """9618_s24_41:3(b) MP1 (D10): required algorithm cannot be delegated to built-ins."""
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
    """9618_s24_41:3(d)(ii) whole (MS p.37): StoreItems, Dequeue once, output actual item."""
    data = '999999X\n1251484\n5500212\n0033585\n9845788\n6666666\n3258746\n8111022\n7568557\n0012353\n'
    completed = run_script(candidate_path, stdin=data, timeout=5.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data)
    assert r.error is None, r.error
    assert r.called('StoreItems') and len(r.called('Dequeue')) == 1
    assert r.calls.index(r.called('StoreItems')[0]) < r.calls.index(r.called('Dequeue')[0])
    assert r.called('Dequeue')[0].result == '999999'
    assert_numbers_in_order(r.stdout, [4, int(r.called('Dequeue')[0].result)])

