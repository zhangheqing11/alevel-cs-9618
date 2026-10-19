# MUTANT 9618_s22_42:2(c)(i) MP2 (recursion / binary-search): the two recursive calls swap their
# bounds (searches the upper half when the middle value is too big).
# Question2_J22 -- reference solution (close to the MS Python example, slips fixed)
import random


# ---- 2(b)(ii) ----
def PrintArray(ArrayData):
    for x in range(0, 10):
        for y in range(0, 10):
            print(ArrayData[x][y], "", end="")
        print("")


# ---- 2(c)(i) ----
def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    # follows the QP pseudocode statement by statement (Mid uses the QP formula)
    if Upper >= Lower:
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
            else:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
    return -1


# ---- main program ----
if __name__ == "__main__":
    # 2(a): local 2D array, 10 x 10 INTEGER, each element random 1..100
    ArrayData = [[0] * 10 for i in range(10)]
    for x in range(0, 10):
        for y in range(0, 10):
            ArrayData[x][y] = random.randint(1, 100)

    # 2(b)(ii): output before sorting
    print("Before")
    PrintArray(ArrayData)

    # 2(b)(i): bubble sort each row (first dimension) into ascending order
    ArrayLength = 10
    for X in range(0, ArrayLength):
        for Y in range(0, ArrayLength - 1):
            for Z in range(0, ArrayLength - Y - 1):
                if ArrayData[X][Z] > ArrayData[X][Z + 1]:
                    TempValue = ArrayData[X][Z]
                    ArrayData[X][Z] = ArrayData[X][Z + 1]
                    ArrayData[X][Z + 1] = TempValue

    # 2(b)(ii): output after sorting
    print("After")
    PrintArray(ArrayData)

    # 2(c)(ii): one number in the first line, one number not in it
    print(BinarySearch(ArrayData, 0, 9, ArrayData[0][2]))
    print(BinarySearch(ArrayData, 0, 9, 0))
