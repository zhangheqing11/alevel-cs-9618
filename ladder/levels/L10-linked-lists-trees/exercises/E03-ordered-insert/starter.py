ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER; -1 is the null pointer
FreePointer = -1          # INTEGER


def InitialiseList() -> None:
    """As in E02: empty the list and link all 6 nodes into the free list."""
    raise NotImplementedError


def OutputList() -> None:
    """As in E02: output each data item in list order, or 'Empty list'."""
    raise NotImplementedError


def InsertInOrder(Item: str) -> bool:
    """Store Item in the first free node and link it in ascending order; False if full."""
    raise NotImplementedError
