PREDICTED = ["Ant Bee Cat Dog", "Elk Ant Bee Cat Dog", "Free: 5"]


def RunTrace() -> None:
    ListData = ["Cat", "Ant", "Dog", "", "Bee", ""]  # STRING, 6 elements
    ListPointer = [2, 4, -1, 5, 0, -1]  # INTEGER, 6 elements
    StartPointer = 1
    FreePointer = 3
    Line = ""
    Current = StartPointer
    while Current != -1:
        Line = Line + ListData[Current] + " "
        Current = ListPointer[Current]
    print(Line)
    NewNode = FreePointer
    FreePointer = ListPointer[NewNode]
    ListData[NewNode] = "Elk"
    ListPointer[NewNode] = StartPointer
    StartPointer = NewNode
    Line = ""
    Current = StartPointer
    while Current != -1:
        Line = Line + ListData[Current] + " "
        Current = ListPointer[Current]
    print(Line)
    print(f"Free: {FreePointer}")


if __name__ == "__main__":
    RunTrace()
