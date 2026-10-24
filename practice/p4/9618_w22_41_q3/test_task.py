"""9618_w22_41 Q3 recursive tree search and postorder."""
import re
import pytest
from testkit import output_lines, run_script

PRESET = [[1,20,5], [2,15,-1], [-1,3,3], [-1,9,4], [-1,10,-1], [-1,58,-1]]


def test_3a_array_shape_and_unused_nodes(sol):
    """9618_w22_41:3(a) MP1/MP3: real 20x3 array; remaining nodes null after part b."""
    assert isinstance(sol.ArrayNodes, list) and len(sol.ArrayNodes) == 20
    assert all(isinstance(row, list) and len(row) == 3 for row in sol.ArrayNodes)
    assert sol.ArrayNodes[6:] == [[-1, -1, -1] for _ in range(14)]


def test_3b_preset_and_pointers(sol):
    """9618_w22_41:3(b) MP1-MP2: six nodes exactly as QP, FreeNode=6, RootPointer=0."""
    assert sol.ArrayNodes[:6] == PRESET
    assert sol.FreeNode == 6 and sol.RootPointer == 0


@pytest.mark.parametrize('value,index', [(20,0), (15,1), (3,2), (9,3), (10,4), (58,5), (1,-1), (59,-1), (8,-1)])
def test_3c_search_both_branches(sol, value, index):
    """9618_w22_41:3(c) MP1 (four completed statements): root return and left/right recursion."""
    assert sol.SearchValue(sol.RootPointer, value) == index
    assert sol.SearchValue(-1, value) == -1


def test_3c_search_recursive_and_null_data(sol, monkeypatch):
    """9618_w22_41:3(c) MP1: recursive search, empty node termination (MP2 structure manual)."""
    calls = []; original = sol.SearchValue
    def spy(root, value):
        calls.append(root); return original(root, value)
    monkeypatch.setattr(sol, 'SearchValue', spy)
    assert sol.SearchValue(0, 10) == 4
    assert calls == [0, 1, 2, 3, 4]
    assert sol.SearchValue(6, 77) == -1


def test_3d_postorder_recursive(sol, monkeypatch, capsys):
    """9618_w22_41:3(d) MP1-MP7: recursive left/right/root; both null-child conditions."""
    calls = []; original = sol.PostOrder
    def spy(root):
        calls.append(root); return original(root)
    monkeypatch.setattr(sol, 'PostOrder', spy)
    sol.PostOrder(sol.ArrayNodes[0])
    assert [int(x) for x in re.findall(r'-?\d+', capsys.readouterr().out)] == [10, 9, 3, 15, 58, 20]
    assert len(calls) >= 6
    sol.PostOrder(sol.ArrayNodes[4])
    assert [int(x) for x in re.findall(r'-?\d+', capsys.readouterr().out)] == [10]


def test_3d_postorder_different_tree(sol, capsys):
    """9618_w22_41:3(d) MP2-MP7: QP illustration postorder 3 9 25 60 50."""
    sol.ArrayNodes = [[1,50,2], [3,25,4], [-1,60,-1], [-1,3,-1], [-1,9,-1]] + [[-1]*3 for _ in range(15)]
    sol.PostOrder(sol.ArrayNodes[0])
    assert [int(x) for x in re.findall(r'-?\d+', capsys.readouterr().out)] == [3,9,25,60,50]


def test_3e_screenshot(candidate_path):
    """9618_w22_41:3(e)(i) MP1-MP3; 3(e)(ii) whole: MS p.23 found1; 10 9 3 15 58 20."""
    r = run_script(candidate_path)
    assert r.returncode == 0, r.stderr
    assert [int(x) for x in re.findall(r'-?\d+', r.stdout)] == [1,10,9,3,15,58,20]
