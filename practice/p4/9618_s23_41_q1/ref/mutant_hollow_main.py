# D46: correct modules, but main hard-codes output without calling them.
# Question1_J2023 -- reference solution (close to the MS Python example)


# ---- 1(b)(i) ----
def PrintArray(DataArray):
    Output = ""
    for X in range(0, len(DataArray)):
        Output = Output + str(DataArray[X]) + " "
    print(Output)


# ---- 1(c) ----
def LinearSearch(DataArray, DataToFind):
    Count = 0
    for X in range(0, len(DataArray)):
        if DataArray[X] == DataToFind:
            Count = Count + 1
    return Count


# ---- main program ----

if __name__ == "__main__":
    print('10 4 5 13 25 31 4 66 12 5 0 11 15 20 21 12 33 49 12 12 7 7 4 22 0 \nEnter a whole number between 0 and 100: The number 12 is found 4 times.\n', end="")
