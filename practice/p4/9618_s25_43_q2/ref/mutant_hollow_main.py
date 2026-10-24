# D46: correct modules, but main hard-codes output without calling them.
def InsertionSort(DataArray):
    if len(DataArray) <= 1:
        return DataArray
    for X in range(1, len(DataArray)):
        CurrentValue = DataArray[X]
        Y = X - 1
        while Y >= 0 and CurrentValue < DataArray[Y]:
            DataArray[Y + 1] = DataArray[Y]
            Y = Y - 1
        DataArray[Y + 1] = CurrentValue
    return DataArray


def OutputArray(DataArray):
    Output = ""
    for Item in DataArray:
        Output = Output + str(Item) + " "
    print(Output)


def Search(DataArray, ItemToFind):
    Low = 0
    High = len(DataArray) - 1
    while Low <= High:
        Middle = (High + Low) // 2
        if DataArray[Middle] < ItemToFind:
            Low = Middle + 1
        elif DataArray[Middle] > ItemToFind:
            High = Middle - 1
        else:
            return Middle
    return -1



if __name__ == "__main__":
    print('0 3 4 56 67 44 43 32 31 345 45 6 54 1 \n0 1 3 4 6 31 32 43 44 45 54 56 67 345 \nData found at 0\nData found at 13\nData found at 12\nData not found\n', end="")
