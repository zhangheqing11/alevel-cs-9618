# M1: intentional fault from spec.md.
PREDICTED = ["Cat Ant Dog Bee", "Cat Ant Dog Elk Bee", "Free: 5"]


def RunTrace() -> None:
    ListData = ["Cat", "Ant", "Dog", "", "Bee", ""]  # STRING, 6 elements
    ListPointer = [2, 4, -1, 5, 0, -1]  # INTEGER, 6 elements
    StartPointer = 1
    FreePointer = 3
    Line = ""
    Current = StartPointer
    for Current in range(6):
        if ListData[Current] != "":
            Line = Line + ListData[Current] + " "
    print(Line)
    NewNode = FreePointer
    FreePointer = ListPointer[NewNode]
    ListData[NewNode] = "Elk"
    ListPointer[NewNode] = StartPointer
    StartPointer = NewNode
    Line = ""
    Current = StartPointer
    for Current in range(6):
        if ListData[Current] != "":
            Line = Line + ListData[Current] + " "
    print(Line)
    print(f"Free: {FreePointer}")


if __name__ == "__main__":
    RunTrace()
