ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER; -1 is the null pointer
FreePointer = -1          # INTEGER


def DeleteItem(Item: str) -> bool:
    """Remove the first node holding Item and add it to the start of the free list."""
    raise NotImplementedError
