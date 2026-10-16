ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER; -1 is the null pointer
FreePointer = -1          # INTEGER


def InitialiseList() -> None:
    """Empty the list and link all 6 nodes into the free list."""
    raise NotImplementedError


def InsertAtStart(Item: str) -> bool:
    """Use the first free node to store Item as the new first node; False if full."""
    raise NotImplementedError


def OutputList() -> None:
    """Output each data item in list order, or 'Empty list'."""
    raise NotImplementedError
