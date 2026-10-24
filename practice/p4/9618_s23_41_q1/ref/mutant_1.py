# MUTANT 9618_s23_41:1(a)(ii) MP3 (type-conversion): stores each line as a string, so
# LinearSearch(DataArray, 12) never matches the integer 12.
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
    # 1(a)(i): local 1D array DataArray, 25 elements of type INTEGER
    DataArray = [0] * 25  # 25 elements, INTEGER

    # 1(a)(ii): read the 25 integers from Data.txt
    try:
        DataFile = open("Data.txt", "r")
        Index = 0
        for Line in DataFile:
            DataArray[Index] = Line.strip()
            Index = Index + 1
        DataFile.close()
    except IOError:
        print("Could not find file")

    # 1(b)(ii)
    PrintArray(DataArray)

    # 1(d)(i)
    DataToFind = int(input("Enter a whole number between 0 and 100: "))
    while DataToFind < 0 or DataToFind > 100:
        DataToFind = int(input("Enter a whole number between 0 and 100: "))
    NumberTimes = LinearSearch(DataArray, DataToFind)
    print("The number", DataToFind, "is found", NumberTimes, "times.")
