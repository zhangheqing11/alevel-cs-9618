# D46: correct modules, but main hard-codes output without calling them.
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
    for X in range(0, 100):
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
    print('Enter a number between 1 and 100 The number appears 2 times\n[2, 2, 3, 4, 6, 7, 8, 8, 8, 11, 13, 14, 14, 16, 18, 19, 21, 22, 23, 25, 25, 26, 26, 26, 27, 27, 29, 30, 33, 34, 34, 35, 36, 37, 38, 40, 40, 40, 41, 41, 41, 43, 44, 47, 49, 49, 50, 51, 52, 52, 53, 53, 54, 54, 54, 56, 58, 58, 58, 59, 59, 60, 60, 61, 61, 63, 64, 65, 69, 69, 69, 70, 70, 70, 72, 72, 73, 73, 74, 75, 75, 78, 79, 80, 81, 82, 82, 83, 84, 85, 86, 88, 92, 94, 98, 99, 99, 99, 100, 100]\n', end="")
