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
    TheArray = [0 for X in range(20)]  # INTEGER array of 20, local to the main program
    TheArray = random.sample(range(0, 101), 20)
    PrintArray(TheArray)
    SortedArray = BubbleSort(TheArray)
    print("Sorted")
    PrintArray(SortedArray)
    DataToFind = int(input("Enter the number to find "))
    Location = RecursiveBinarySearch(SortedArray, 0, 19, DataToFind)
    if Location == -1:
        print("Not found")
    else:
        print("Found at position", Location)
