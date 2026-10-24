# 9618_s25_41:2(a) MP8 and 2(c) MP5; exception-handling
def ReadData():
    # DataList: 1D ARRAY OF STRING, length determined by the input file.
    DataList = []
    FileName = input("Enter the filename: ")
    try:
        File = open(FileName, "r")
        for Line in File:
            DataList.append(Line.rstrip("\r\n"))
        File.close()
    except ValueError:
        print("Cannot open or read file")
    return DataList


def SplitData(DataArray):
    # Six 1D INTEGER arrays; each grows to the number of items of that colour.
    Red = []
    Green = []
    Blue = []
    Orange = []
    Yellow = []
    Pink = []
    for Line in DataArray:
        SplitLine = Line.split(",")
        Number = int(SplitLine[0])
        if SplitLine[1] == "red":
            Red.append(Number)
        elif SplitLine[1] == "green":
            Green.append(Number)
        elif SplitLine[1] == "blue":
            Blue.append(Number)
        elif SplitLine[1] == "orange":
            Orange.append(Number)
        elif SplitLine[1] == "yellow":
            Yellow.append(Number)
        else:
            Pink.append(Number)
    StoreData(Red, "Red.txt")
    StoreData(Green, "Green.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Yellow, "Yellow.txt")
    StoreData(Pink, "Pink.txt")


def StoreData(DataToStore, FileName):
    try:
        File = open(FileName, "a")
        for Item in DataToStore:
            File.write(str(Item))
            File.write("\n")
        File.close()
    except ValueError:
        print("Cannot create or write to file")


if __name__ == "__main__":
    DataFromFile = ReadData()
    SplitData(DataFromFile)
