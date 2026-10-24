# 9618_s24_42:3(c)(i) MP2–MP4; insertion-sort
def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    RecursiveInsertion(IntegerArray, NumberElements - 1)
    LastItem = IntegerArray[NumberElements - 1]
    CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem:
        LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray


def IterativeInsertion(IntegerArray, NumberElements):
    # Process growing prefixes, in the same order as recursion unwinds.
    for Position in range(NumberElements - 1, -1, -1):
        LastItem = IntegerArray[Position]
        CheckItem = Position - 1
        LoopAgain = True
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
        while LoopAgain:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem = CheckItem - 1
            if CheckItem < 0:
                LoopAgain = False
            elif IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
        IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray


def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    Middle = (Last + First) // 2
    if IntegerArray[Middle] == ToFind:
        return Middle
    elif IntegerArray[Middle] > ToFind:
        return BinarySearch(IntegerArray, First, Middle - 1, ToFind)
    else:
        return BinarySearch(IntegerArray, Middle + 1, Last, ToFind)


if __name__ == "__main__":
    # NumberArray: ARRAY[0:6] OF INTEGER, local to the main program.
    NumberArray = [100, 85, 644, 22, 15, 8, 1]
    SortedArray = RecursiveInsertion(NumberArray.copy(), len(NumberArray))
    print("Recursive", SortedArray)
    Sorted2Array = IterativeInsertion(NumberArray.copy(), len(NumberArray))
    print("Iterative", Sorted2Array)
    Position = BinarySearch(Sorted2Array, 0, len(NumberArray) - 1, 644)
    if Position == -1:
        print("Not found")
    else:
        print(Position)
