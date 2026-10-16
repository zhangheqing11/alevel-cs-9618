# M1: intentional fault from spec.md.
ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER; -1 is the null pointer
FreePointer = -1          # INTEGER


def DeleteItem(Item: str) -> bool:
    global StartPointer, FreePointer
    Previous = -1
    Current = StartPointer
    while Current != -1 and ListData[Current] != Item:
        Previous = Current
        Current = ListPointer[Current]
    if Current == -1:
        return False
    ListPointer[Previous] = ListPointer[Current]
    ListPointer[Current] = FreePointer
    FreePointer = Current
    return True
