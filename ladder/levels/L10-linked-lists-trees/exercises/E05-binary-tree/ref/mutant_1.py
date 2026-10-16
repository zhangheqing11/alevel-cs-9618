# M1: intentional fault from spec.md.
LeftPointer = [-1] * 10   # INTEGER, 10 elements
TreeData = [-1] * 10      # INTEGER, 10 elements
RightPointer = [-1] * 10  # INTEGER, 10 elements
RootPointer = -1          # INTEGER; -1 means the tree is empty
FreeNode = 0              # INTEGER; index of the next unused element


def InsertNode(Item: int) -> bool:
    global RootPointer, FreeNode
    if FreeNode == 10:
        return False
    TreeData[FreeNode] = Item
    LeftPointer[FreeNode] = -1
    RightPointer[FreeNode] = -1
    if RootPointer == -1:
        RootPointer = FreeNode
    else:
        Current = RootPointer
        while True:
            if Item > TreeData[Current]:
                if LeftPointer[Current] == -1:
                    LeftPointer[Current] = FreeNode
                    break
                Current = LeftPointer[Current]
            else:
                if RightPointer[Current] == -1:
                    RightPointer[Current] = FreeNode
                    break
                Current = RightPointer[Current]
    FreeNode = FreeNode + 1
    return True


def SearchTree(Item: int) -> int:
    Current = RootPointer
    while Current != -1:
        if TreeData[Current] == Item:
            return Current
        if Item > TreeData[Current]:
            Current = LeftPointer[Current]
        else:
            Current = RightPointer[Current]
    return -1
