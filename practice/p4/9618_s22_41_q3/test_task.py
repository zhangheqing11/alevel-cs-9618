"""Circular queue tests derived from the matching 9618_s22_41 MS."""
from testkit import output_lines, run_script


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
    """9618_s22_41:3(d)(i) MP1-MP5; 3(d)(ii) whole: ten successes, one failure, A then B."""
    r = run_script(candidate_path, stdin='\n'.join('ABCDEFGHIJK') + '\n')
    assert r.returncode == 0, r.stderr
    lines = output_lines(r.stdout)
    assert len(lines) == 13
    # QP permits any appropriate message; ten equal outcomes then a different outcome.
    status = [line.rsplit(':', 1)[-1].strip() for line in lines[:11]]
    assert len(set(status[:10])) == 1 and status[10] != status[0]
    assert lines[-2].strip().endswith('A') and lines[-1].strip().endswith('B')
