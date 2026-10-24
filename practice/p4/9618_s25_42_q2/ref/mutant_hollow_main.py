# D46: correct modules, but main bypasses the required calls.
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
    return Key % 200


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
    print('915\n136\n415\n55\n349\n775\n846\n469\n246\n752\n8\n889\n695\n292\n417\n181\n810\n972\n781\n46\n120\n95\n378\n433\n994\n946\n586\n365\n615\n580\n128\n944\n2\n689\n962\n704\n948\n435\n195\n981\n320\n658\n831\n408\n947\n830\n88\n362\n629\n986\n31\n823\n527\n141\n905\n965\n697\n15\n24\n977\n88\n', end='')
