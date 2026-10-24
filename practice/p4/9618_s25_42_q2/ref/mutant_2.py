# 9618_s25_42:2(c) MP2 div-mod: wrong modulus.
class NewRecord:
    def __init__(self, pKey, pItem1, pItem2):
        self.__Key = pKey  # INTEGER
        self.__Item1 = pItem1  # INTEGER
        self.__Item2 = pItem2  # INTEGER

    def GetKey(self):
        return self.__Key

    def GetItem1(self):
        return self.__Item1

    def GetItem2(self):
        return self.__Item2


HashTable = [None] * 200  # ARRAY[0:199] OF NewRecord
Spare = [None] * 100  # ARRAY[0:99] OF NewRecord


def Initialise():
    for X in range(200):
        HashTable[X] = NewRecord(-1, -1, -1)
    for X in range(100):
        Spare[X] = NewRecord(-1, -1, -1)


def CalculateHash(Key):
    return Key % 199


def InsertIntoHash(TheRecord):
    HashValue = CalculateHash(TheRecord.GetKey())
    if HashTable[HashValue].GetKey() == -1:
        HashTable[HashValue] = TheRecord
    else:
        for x in range(100):
            if Spare[x].GetKey() == -1:
                Spare[x] = TheRecord
                break


def CreateHashTable():
    try:
        File = open('HashData.txt', 'r')
        for Line in File:
            Data = Line.strip().split(',')
            InsertIntoHash(NewRecord(int(Data[0]), int(Data[1]), int(Data[2])))
        File.close()
    except OSError:
        print('Cannot open file')


def PrintSpare():
    X = 0
    while X < 100 and Spare[X].GetKey() != -1:
        print(Spare[X].GetKey())
        X += 1


if __name__ == '__main__':
    Initialise()
    CreateHashTable()
    PrintSpare()
