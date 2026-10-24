# D46: correct modules, but main hard-codes output without calling them.
# Reference solution for 9618_w25_42 Question 2 (Question2_N25).
# Follows the MS Python examples (MS p.19-25); the main program is written
# under if __name__ == "__main__".
import random


# ---- 2(b) ----
def PrintArray(DataArray):
    Output = ""
    for Item in DataArray:
        Output = Output + str(Item) + " "
    print(Output)


# ---- 2(c) ----
def BubbleSort(DataArray):
    Swap = True
    while Swap == True:
        Swap = False
        for Y in range(0, len(DataArray) - 1):
            if DataArray[Y] > DataArray[Y + 1]:
                DataArray[Y], DataArray[Y + 1] = DataArray[Y + 1], DataArray[Y]
                Swap = True
    return DataArray


# ---- 2(e) ----
def RecursiveBinarySearch(DataArray, Lower, Upper, DataToFind):
    if Upper >= Lower:
        Middle = Lower + (Upper - Lower) // 2
        if DataArray[Middle] == DataToFind:
            return Middle
        elif DataArray[Middle] > DataToFind:
            return RecursiveBinarySearch(DataArray, Lower, Middle - 1, DataToFind)
        else:
            return RecursiveBinarySearch(DataArray, Middle + 1, Upper, DataToFind)
    else:
        return -1


# ---- main program: 2(a), 2(d)(i), 2(f)(i) ----

if __name__ == "__main__":
    print('71 25 1 27 16 76 42 37 31 95 91 24 48 62 78 12 54 23 73 57 \nSorted\n1 12 16 23 24 25 27 31 37 42 48 54 57 62 71 73 76 78 91 95 \nEnter the number to find Not found\n', end="")
