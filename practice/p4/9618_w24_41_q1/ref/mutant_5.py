# Mutant: 9618_w24_41:1(d)(i) MP3 (bubble-sort, loop-bounds) - inner loop stops one pair early.
# Reference solution for 9618_w24_41 Question 1 (Question1_N24).
# Follows the MS Python examples; ReadData() builds the 45-element array first
# (D10 ①) and reads it line by line with the newline removed, returning the
# array after the try (the MS example returns nothing when the file is missing).

# ---- 1(a) ----
def ReadData():
    Colours = ["" for X in range(45)]  # local array of 45 STRING
    try:
        File = open("Data.txt", "r")
        for X in range(45):
            Colours[X] = File.readline().strip()
        File.close()
    except IOError:
        print("No file found")
    return Colours


# ---- 1(b)(i) ----
def FormatArray(DataArray):
    OutputText = ""
    for X in range(0, 45):
        OutputText = OutputText + DataArray[X] + " "
    return OutputText


# ---- 1(c) ----
def CompareStrings(First, Second):
    Count = 0
    while True:
        if First[Count] < Second[Count]:
            return 1
        elif First[Count] > Second[Count]:
            return 2
        else:
            Count = Count + 1


# ---- 1(d)(i) ----
def Bubble(DataArray):
    ArrayLength = len(DataArray)
    for X in range(ArrayLength - 1):
        for Y in range(0, ArrayLength - X - 2):
            Result = CompareStrings(DataArray[Y], DataArray[Y + 1])
            if Result == 2:
                DataArray[Y], DataArray[Y + 1] = DataArray[Y + 1], DataArray[Y]
    return DataArray


# ---- main program: 1(b)(ii), 1(d)(ii) ----
if __name__ == "__main__":
    Colours = ReadData()  # STRING array
    print(FormatArray(Colours))
    BubbleSorted = Bubble(Colours)
    print(FormatArray(BubbleSorted))
