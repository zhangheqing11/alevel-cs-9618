LeftPointer = [-1] * 10   # INTEGER, 10 elements
TreeData = [-1] * 10      # INTEGER, 10 elements
RightPointer = [-1] * 10  # INTEGER, 10 elements
RootPointer = -1          # INTEGER; -1 means the tree is empty
FreeNode = 0              # INTEGER; index of the next unused element


def InsertNode(Item: int) -> bool:
    """Store Item in element FreeNode and link it into the tree; False if full."""
    raise NotImplementedError


def SearchTree(Item: int) -> int:
    """Return the index of the node holding Item, or -1."""
    raise NotImplementedError
