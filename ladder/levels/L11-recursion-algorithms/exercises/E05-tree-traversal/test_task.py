import pytest
from testkit import output_lines


def call_counted(sol, monkeypatch, name, *args):
    original = getattr(sol, name)
    calls = 0

    def wrapper(*values):
        nonlocal calls
        calls += 1
        return original(*values)

    with monkeypatch.context() as patch:
        patch.setattr(sol, name, wrapper)
        result = getattr(sol, name)(*args)
    return result, calls


def set_tree(sol, chain=False):
    sol.RootPointer = 0
    if chain:
        sol.TreeData = [1, 2, 3, 4, 5] + [-1] * 5
        sol.LeftPointer = [-1] * 10
        sol.RightPointer = [1, 2, 3, 4] + [-1] * 6
    else:
        sol.TreeData = [50, 30, 70, 20, 40, 60] + [-1] * 4
        sol.LeftPointer = [1, 3, 5] + [-1] * 7
        sol.RightPointer = [2, 4] + [-1] * 8


@pytest.mark.parametrize("node, expected", [(0, ["20", "30", "40", "50", "60", "70"]), (1, ["20", "30", "40"]), (-1, [])])
def test_in_order(sol, capsys, node, expected):
    """B1-B2: complete in-order output for root/subtree and none for empty pointer."""
    set_tree(sol)
    sol.InOrder(node)
    assert output_lines(capsys.readouterr().out) == expected


def test_counts_and_heights(sol):
    """B3-B4: count and height for root, subtrees, leaf and null pointer."""
    set_tree(sol)
    for node, expected in [(0, 6), (1, 3), (-1, 0)]:
        assert sol.CountNodes(node) == expected
    for node, expected in [(0, 3), (2, 2), (3, 1), (-1, 0)]:
        assert sol.TreeHeight(node) == expected


def test_chain(sol, capsys):
    """B5: a degenerate five-node tree has five outputs, five nodes and height five."""
    set_tree(sol, chain=True)
    sol.InOrder(0)
    assert output_lines(capsys.readouterr().out) == ["1", "2", "3", "4", "5"]
    assert sol.CountNodes(0) == 5
    assert sol.TreeHeight(0) == 5


@pytest.mark.parametrize("name", ["InOrder", "CountNodes", "TreeHeight"])
def test_recursive_modules(sol, monkeypatch, name):
    """B6: each module recurses through its own module-level name, wrapper restored."""
    set_tree(sol)
    _, calls = call_counted(sol, monkeypatch, name, 0)
    assert calls >= 2
