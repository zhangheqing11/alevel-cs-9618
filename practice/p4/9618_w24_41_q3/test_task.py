"""w24/41 Q3: linked nodes, free list and first-match deletion."""
import re
import pytest
from testkit import feed_input, run_script, run_script_traced


def chain(sol, start):
    indices = []
    while start != -1:
        assert 0 <= start < 20 and start not in indices, 'invalid pointer or cycle'
        indices.append(start)
        start = sol.LinkedList[start][1]
    return indices


def values(sol):
    return [sol.LinkedList[i][0] for i in chain(sol, sol.FirstNode)]


def check_partition(sol):
    used = chain(sol, sol.FirstNode)
    free = chain(sol, sol.FirstEmpty)
    assert set(used).isdisjoint(free)
    assert set(used + free) == set(range(20)), 'lost nodes in the free/used lists'


def test_3a_initial_free_list(sol):
    """9618_w24_41:3(a) MP1-MP2: all 20 nodes, terminating -1 and initial pointers."""
    assert sol.FirstNode == -1 and sol.FirstEmpty == 0
    assert isinstance(sol.LinkedList, list) and len(sol.LinkedList) >= 20
    assert all(isinstance(row, list) and len(row) >= 2 for row in sol.LinkedList[:20])
    assert [row[:2] for row in sol.LinkedList[:20]] == [[-1, i + 1] for i in range(19)] + [[-1, -1]]


def test_3b_insert_five_at_front(sol, monkeypatch):
    """9618_w24_41:3(b) MP1-MP7: each new node is prepended, next free saved first."""
    feed_input(monkeypatch, '5', '1', '2', '3', '8')
    sol.InsertData()
    assert values(sol) == [8, 3, 2, 1, 5]
    assert sol.FirstNode == 4 and sol.FirstEmpty == 5
    check_partition(sol)


def test_3b_full_and_recycled_nodes(sol, monkeypatch):
    """9618_w24_41:3(b) MP2-MP7; 3(d)(i) MP8: capacity and returned nodes reused."""
    for group in range(4):
        feed_input(monkeypatch, *(str(i) for i in range(group * 5 + 1, group * 5 + 6)))
        sol.InsertData()
    assert sol.FirstEmpty == -1 and values(sol) == list(range(20, 0, -1))
    before = [r[:] for r in sol.LinkedList]
    feed_input(monkeypatch, *(['99'] * 5))
    sol.InsertData()
    assert sol.LinkedList == before
    check_partition(sol)
    sol.RemoveData(10)
    check_partition(sol)
    feed_input(monkeypatch, *(['77'] * 5))
    sol.InsertData()
    assert values(sol) == [77] + [i for i in range(20, 0, -1) if i != 10]
    assert sol.FirstEmpty == -1
    check_partition(sol)


def test_3c_i_output_follows_nonsequential_pointers(sol, capsys):
    """9618_w24_41:3(c)(i) MP1-MP2: traversal begins at FirstNode, follows pointers."""
    sol.LinkedList[7] = [51, 2]
    sol.LinkedList[2] = [14, 12]
    sol.LinkedList[12] = [86, -1]
    sol.FirstNode = 7
    sol.OutputLinkedList()
    assert_numbers_in_order(capsys.readouterr().out, [51, 14, 86])


@pytest.mark.parametrize('target,expected', [(8, [3, 2, 1, 5]), (2, [8, 3, 1, 5]), (5, [8, 3, 2, 1])])
def test_3d_i_remove_head_middle_tail(sol, monkeypatch, target, expected):
    """9618_w24_41:3(d)(i) MP2-MP8: unlink correctly and return node to free list."""
    feed_input(monkeypatch, '5', '1', '2', '3', '8')
    sol.InsertData()
    assert values(sol) == [8, 3, 2, 1, 5]
    sol.RemoveData(target)
    assert values(sol) == expected
    check_partition(sol)


def test_3d_i_duplicate_only_first_removed(sol, monkeypatch):
    """9618_w24_41:3(d)(i) MP2-MP8: only the first occurrence from FirstNode."""
    feed_input(monkeypatch, '5', '6', '8', '9', '5')
    sol.InsertData()
    sol.RemoveData(5)
    assert values(sol) == [9, 8, 6, 5]
    check_partition(sol)


def test_3c_iii_screenshot_reverse(candidate_path):
    """9618_w24_41:3(c)(ii) whole; 3(c)(iii) whole: 8 3 2 1 5."""
    result = run_script(candidate_path, stdin='5\n1\n2\n3\n8\n', timeout=1.0)
    assert result.returncode == 0, result.stderr
    before = result.stdout.split('After')[0]
    assert_numbers_in_order(before, [8, 3, 2, 1, 5])


@pytest.mark.parametrize('data,expected', [('5\n6\n8\n9\n5\n', [9, 8, 6, 5]),
                                         ('10\n7\n8\n5\n6\n', [6, 8, 7, 10])])
def test_3d_iii_screenshot_after(candidate_path, data, expected):
    """9618_w24_41:3(d)(ii) whole; 3(d)(iii) whole: both official data sets."""
    result = run_script(candidate_path, stdin=data, timeout=1.0)
    assert result.returncode == 0, result.stderr
    assert 'After' in result.stdout
    assert_numbers_in_order(result.stdout.split('After')[-1], expected)


def assert_numbers_in_order(text, expected):
    """D31/D46: allow explanatory numbers and line breaks around required values."""
    values = iter(float(n) for n in re.findall(r"(?<![\w.])-?\d+(?:\.\d+)?(?![\w.])", text))
    for wanted in expected:
        assert any(value == wanted for value in values), f"missing ordered value {wanted}: {text!r}"


@pytest.mark.parametrize('data', ['5\n1\n2\n3\n8\n', '5\n6\n8\n9\n5\n', '10\n7\n8\n5\n6\n'])
def test_3c_ii_3d_ii_main_call_chain(candidate_path, data):
    """9618_w24_41:3(c)(ii),3(d)(ii) whole (MS pp.32/36): insert, output, RemoveData(5), output."""
    completed = run_script(candidate_path, stdin=data, timeout=5.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data)
    assert r.error is None, r.error
    names = [c.name for c in r.calls if c.name in ('InsertData', 'OutputLinkedList', 'RemoveData')]
    assert names == ['InsertData', 'OutputLinkedList', 'RemoveData', 'OutputLinkedList']
    assert r.called('RemoveData')[0].args.get('ItemToRemove') == 5
    before, after = r.stdout.split('After', 1)
    expected = list(reversed([int(x) for x in data.split()]))
    assert_numbers_in_order(before, expected)
    expected.remove(5)
    assert_numbers_in_order(after, expected)
