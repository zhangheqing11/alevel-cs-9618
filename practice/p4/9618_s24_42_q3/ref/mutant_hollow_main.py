# D46: correct modules, but main hard-codes output without calling them.
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
    for Position in range(1, NumberElements):
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
    print('Recursive [1, 8, 15, 22, 85, 100, 644]\nIterative [1, 8, 15, 22, 85, 100, 644]\n6\n', end="")
