# Mutant: 9618_w22_41:1(c) MP4 (loop-bounds) - range(0, 99) misses the last element (the MS example's own slip).
# Reference solution for 9618_w22_41 Question 1 (Question1_N22).
# Follows the MS Python example; fixes: FindValues loops all 100 elements
# (the MS example uses range(0, 99)), the stray rstrip line is folded into
# the int() conversion, and BubbleSort prints the array itself (QP 1(e)).

# ---- 1(a) ----
DataArray = [0 for I in range(100)]  # global 1D array of 100 INTEGER


# ---- 1(b) ----
def ReadFile():
    global DataArray
    try:
        TextFile = "IntegerData.txt"
        File = open(TextFile, 'r')
        for X in range(0, 100):
            DataArray[X] = int(File.readline().strip())
        File.close()
    except IOError:
        print("Could not find file")


# ---- 1(c) ----
def FindValues():
    global DataArray
    DataToFind = -1
    while DataToFind < 1 or DataToFind > 100:
        DataToFind = int(input("Enter a number between 1 and 100 "))
    Total = 0
    for X in range(0, 99):
        if DataArray[X] == DataToFind:
            Total = Total + 1
    return Total


# ---- 1(e) ----
def BubbleSort():
    global DataArray
    N = 100
    for I in range(N - 1):
        for J in range(0, N - I - 1):
            if DataArray[J] > DataArray[J + 1]:
                DataArray[J], DataArray[J + 1] = DataArray[J + 1], DataArray[J]
    print(DataArray)


# ---- main program: 1(d)(i), 1(e) ----
if __name__ == "__main__":
    ReadFile()
    print("The number appears " + str(FindValues()) + " times")
    BubbleSort()
