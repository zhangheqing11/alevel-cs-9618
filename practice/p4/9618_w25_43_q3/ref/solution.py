# Reference solution for 9618_w25_43 Question 3 (Question3_N25).
# Follows the MS Python examples (MS p.33-38), including the MS parameter order
# RecursiveCount(DataToFind, ArrayCopy, NumberElements); the QP lists the
# parameters as ArrayCopy, NumberElements, DataToFind - either order is fine
# as long as the QP identifiers are used.

# ---- 3(a)(i) ----
def RecursiveCount(DataToFind, ArrayCopy, NumberElements):
    if NumberElements > 0:
        NewArray = ArrayCopy[1:]
        if ArrayCopy[0] == DataToFind:
            return 1 + RecursiveCount(DataToFind, NewArray, NumberElements - 1)
        else:
            return RecursiveCount(DataToFind, NewArray, NumberElements - 1)
    else:
        return 0


# ---- 3(b)(ii) ----
def SplitData(DataString):
    SplitDataArray = []  # array of STRING, one statement per element
    Count = 0
    for X in range(4):
        TempString = ""
        Character = DataString[Count]
        while Character != ";":
            TempString = TempString + Character
            Count = Count + 1
            Character = DataString[Count]
        SplitDataArray.append(TempString)
        Count = Count + 1
    return SplitDataArray


# ---- main program: 3(a)(ii), 3(b)(i), 3(b)(iii) ----
if __name__ == "__main__":
    MyArray = [0, 5, 1, 2, 5, 9, 9, 6, 5, 0]  # 1D array of 10 INTEGER
    print(RecursiveCount(0, MyArray, 10))
    Code = "x=0;y=1;x=x+y;y++;"  # STRING, local to the main program
    SplitDataArray = SplitData(Code)
    for X in range(4):
        print(SplitDataArray[X])
