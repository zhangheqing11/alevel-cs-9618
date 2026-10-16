LeftPointer = [-1] * 10   # INTEGER, 10 elements
TreeData = [-1] * 10      # INTEGER, 10 elements
RightPointer = [-1] * 10  # INTEGER, 10 elements
RootPointer = -1          # INTEGER; -1 means the tree is empty


def InOrder(NodePointer: int) -> None:
    """Output the subtree rooted at NodePointer in order, one value per line."""
    raise NotImplementedError


def CountNodes(NodePointer: int) -> int:
    """Return the number of nodes in the subtree rooted at NodePointer."""
    raise NotImplementedError


def TreeHeight(NodePointer: int) -> int:
    """Return the height of the subtree rooted at NodePointer (0 if empty)."""
    raise NotImplementedError
