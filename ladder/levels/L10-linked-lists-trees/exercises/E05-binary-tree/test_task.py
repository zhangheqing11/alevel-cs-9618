def build_tree(sol):
    for item in [50, 30, 70, 20, 40, 60]:
        assert sol.InsertNode(item) is True


def test_empty_and_root(sol):
    """B1-B2: search an empty tree, then first insertion establishes its root."""
    assert sol.SearchTree(5) == -1
    assert sol.InsertNode(50) is True
    assert sol.RootPointer == 0
    assert sol.FreeNode == 1


def test_structure_and_search(sol):
    """B3-B5: insertion updates parent links; searches find root/deeper nodes or report absent."""
    build_tree(sol)
    assert sol.TreeData[:6] == [50, 30, 70, 20, 40, 60]
    assert sol.LeftPointer[:6] == [1, 3, 5, -1, -1, -1]
    assert sol.RightPointer[:6] == [2, 4, -1, -1, -1, -1]
    assert sol.FreeNode == 6
    for value, index in [(40, 4), (60, 5), (50, 0), (20, 3), (65, -1), (10, -1)]:
        assert sol.SearchTree(value) == index


def test_equal_value(sol):
    """B6: equal values go right, consume a node and search still finds the first match."""
    build_tree(sol)
    assert sol.InsertNode(30) is True
    assert sol.FreeNode == 7
    assert sol.TreeData[6] == 30
    assert sol.LeftPointer[4] == 6
    assert sol.SearchTree(30) == 1


def test_full(sol):
    """B7: ten nodes fit, eleventh is rejected and existing search path is retained."""
    for value in range(10):
        assert sol.InsertNode(value) is True
    assert sol.InsertNode(10) is False
    assert sol.SearchTree(5) == 5
