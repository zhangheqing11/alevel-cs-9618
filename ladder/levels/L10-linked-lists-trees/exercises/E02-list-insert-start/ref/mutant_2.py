# M2: intentional fault from spec.md.
ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER; -1 is the null pointer
FreePointer = -1          # INTEGER


def InitialiseList() -> None:
    global StartPointer, FreePointer
    for Index in range(6):
        ListData[Index] = ""
        ListPointer[Index] = Index + 1
    ListPointer[5] = -1
    StartPointer = -1
    FreePointer = 0


def OutputList() -> None:
    Current = StartPointer
    if Current == -1:
        print("Empty list")
    Visits = 0
    while Current != -1 and Visits < 6:
        Visits = Visits + 1
        print(ListData[Current])
        Current = ListPointer[Current]


def InsertAtStart(Item: str) -> bool:
    global StartPointer, FreePointer
    if FreePointer == -1:
        return False
    NewNode = FreePointer
    ListData[NewNode] = Item
    ListPointer[NewNode] = StartPointer
    StartPointer = NewNode
    return True
