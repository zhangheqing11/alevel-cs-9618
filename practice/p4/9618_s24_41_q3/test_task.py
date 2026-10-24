"""9618_s24_41 Q3 linear queue and weighted check digit."""
import re
from testkit import feed_input, output_lines, run_script

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
    assert re.search(r'\b4\b', output_lines(capsys.readouterr().out)[-1])


def test_3d_x_and_numeric_checks_at_full_queue(sol, monkeypatch, capsys):
    """9618_s24_41:3(d)(i) MP4-MP8: wrong X rejected; valid X accepted even when full."""
    sol.QueueTail = 19; sol.QueueHead = 0
    feed_input(monkeypatch, *(['954123X', '999999X'] * 5))
    sol.StoreItems()
    out = output_lines(capsys.readouterr().out)
    assert len(out) >= 6 and re.search(r'\b5\b', out[-1])
    assert sol.QueueTail == 19


def test_3d_screenshot(candidate_path):
    """9618_s24_41:3(d)(ii) whole; 3(d)(iii) MP1-MP2: four invalid, item code 999999."""
    r = run_script(candidate_path, stdin='\n'.join(DATA) + '\n')
    assert r.returncode == 0, r.stderr
    lines = output_lines(r.stdout)
    assert re.search(r'\b4\b', lines[-2])
    assert re.search(r'\b999999\b', lines[-1])


def test_3d_main_empty_message(candidate_path):
    """9618_s24_41:3(d)(ii) whole: suitable message after all ten inputs are invalid."""
    r = run_script(candidate_path, stdin=('9541235\n' * 10))
    assert r.returncode == 0, r.stderr
    lines = output_lines(r.stdout)
    assert re.search(r'\b10\b', lines[-2])
    assert lines[-1].strip() and '954123' not in lines[-1]
