LeftPointer = [-1] * 10   # INTEGER, 10 elements
TreeData = [-1] * 10      # INTEGER, 10 elements
RightPointer = [-1] * 10  # INTEGER, 10 elements
RootPointer = -1          # INTEGER; -1 means the tree is empty


def InOrder(NodePointer: int) -> None:
    if NodePointer != -1:
        InOrder(LeftPointer[NodePointer])
        print(TreeData[NodePointer])
        InOrder(RightPointer[NodePointer])


def CountNodes(NodePointer: int) -> int:
    if NodePointer == -1:
        return 0
    return 1 + CountNodes(LeftPointer[NodePointer]) + CountNodes(RightPointer[NodePointer])


def TreeHeight(NodePointer: int) -> int:
    if NodePointer == -1:
        return 0
    LeftHeight = TreeHeight(LeftPointer[NodePointer])
    RightHeight = TreeHeight(RightPointer[NodePointer])
    if LeftHeight > RightHeight:
        return 1 + LeftHeight
    return 1 + RightHeight
