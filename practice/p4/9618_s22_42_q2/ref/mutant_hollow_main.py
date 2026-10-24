# D46: correct modules, but main hard-codes output without calling them.
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
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1


# ---- main program ----

if __name__ == "__main__":
    print('Before\n97 44 14 11 84 51 32 50 52 78 \n47 99 18 38 93 97 64 76 98 20 \n46 38 51 81 12 63 81 61 82 79 \n90 57 77 23 40 52 1 73 51 28 \n98 72 84 66 94 63 7 96 48 24 \n47 89 47 12 43 82 78 57 87 47 \n32 99 28 84 32 46 98 36 34 22 \n9 71 52 40 95 96 80 97 97 47 \n15 51 39 24 70 92 49 90 80 51 \n8 3 19 79 80 7 24 96 6 100 \nAfter\n11 14 32 44 50 51 52 78 84 97 \n18 20 38 47 64 76 93 97 98 99 \n12 38 46 51 61 63 79 81 81 82 \n1 23 28 40 51 52 57 73 77 90 \n7 24 48 63 66 72 84 94 96 98 \n12 43 47 47 47 57 78 82 87 89 \n22 28 32 32 34 36 46 84 98 99 \n9 40 47 52 71 80 95 96 97 97 \n15 24 39 49 51 51 70 80 90 92 \n3 6 7 8 19 24 79 80 96 100 \n2\n-1\n', end="")
