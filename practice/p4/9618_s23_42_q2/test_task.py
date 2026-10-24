"""9618_s23_42 Q2 sale-record circular queue."""
import re
from testkit import feed_input, run_script


def record(value):
    return None if value is None else (value.SaleID, value.Quantity)


def test_2a_record(sol):
    """9618_s23_42:2(a) MP2: constructor stores both attributes."""
    assert record(sol.SaleData('ABC', 2)) == ('ABC', 2)


def test_2b_initial_state(sol):
    """9618_s23_42:2(b) MP1-MP4: five empty records and pointers/count zero."""
    assert len(sol.CircularQueue) == 5
    assert [record(v) for v in sol.CircularQueue] == [('', -1)] * 5
    assert (sol.Head, sol.Tail, sol.NumberOfItems) == (0, 0, 0)


def test_2c_enqueue_full_wrap(sol):
    """9618_s23_42:2(c) MP2-MP6: store, increment, wrap, full returns -1."""
    for i in range(5):
        assert sol.Enqueue(sol.SaleData(str(i), i)) == 1
        assert record(sol.CircularQueue[i]) == (str(i), i)
        assert (sol.Head, sol.Tail, sol.NumberOfItems) == (0, (i + 1) % 5, i + 1)
    before = [record(x) for x in sol.CircularQueue]
    assert sol.Enqueue(sol.SaleData('full', 99)) == -1
    assert [record(x) for x in sol.CircularQueue] == before
    assert (sol.Head, sol.Tail, sol.NumberOfItems) == (0, 0, 5)


def test_2d_dequeue_empty_fifo_reuse(sol):
    """9618_s23_42:2(d) MP2-MP6: null/empty record accepted, FIFO and head wrap."""
    assert record(sol.Dequeue()) in [None, ('', -1)]
    assert (sol.Head, sol.Tail, sol.NumberOfItems) == (0, 0, 0)
    for cycle in range(3):
        for i in range(5):
            assert sol.Enqueue(sol.SaleData(f'{cycle}:{i}', i)) == 1
        for i in range(5):
            assert record(sol.Dequeue()) == (f'{cycle}:{i}', i)
            assert (sol.Head, sol.NumberOfItems) == ((i + 1) % 5, 4 - i)
    assert record(sol.Dequeue()) in [None, ('', -1)]


def test_2e_enter_record_stored_and_full(sol, monkeypatch, capsys):
    """9618_s23_42:2(e) MP2-MP5: numeric quantity, enqueue record, branch on result."""
    calls = []
    original = sol.Enqueue
    def spy(value):
        calls.append(record(value)); return original(value)
    monkeypatch.setattr(sol, 'Enqueue', spy)
    for i in range(6):
        feed_input(monkeypatch, f'ID{i}', str(i + 1))
        sol.EnterRecord()
        assert ('Stored' if i < 5 else 'Full') in capsys.readouterr().out
    assert calls == [(f'ID{i}', i + 1) for i in range(6)]


def test_2f_screenshot(candidate_path):
    """9618_s23_42:2(f)(i) MP1-MP5 max4; 2(f)(ii) whole: own-MS records and statuses."""
    data = [('ADF', 10), ('OOP', 1), ('BXW', 5), ('XXZ', 22), ('HQR', 6), ('LLP', 3), ('LLP', 3)]
    r = run_script(candidate_path, stdin=''.join(f'{a}\n{b}\n' for a, b in data))
    assert r.returncode == 0, r.stderr
    assert re.findall(r'Stored|Full', r.stdout) == ['Stored'] * 5 + ['Full', 'Stored']
    pairs = [(a, int(b)) for a, b in re.findall(r'\b(ADF|OOP|BXW|XXZ|HQR|LLP)\s+(-?\d+)\b', r.stdout)]
    assert pairs == [('ADF', 10), ('LLP', 3), ('OOP', 1), ('BXW', 5), ('XXZ', 22), ('HQR', 6)]
