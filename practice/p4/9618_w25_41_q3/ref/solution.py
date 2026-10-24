class Record:
    def __init__(self, pKey, pData):
        self.Key = pKey  # INTEGER, public
        self.Data = pData  # STRING, public


# HashTable: ARRAY[0:99, 0:9] OF Record (null until initialised).
HashTable = [[None for Y in range(10)] for X in range(100)]


def InitialiseHashTable():
    global HashTable
    HashTable = [[Record(-1, '') for Y in range(10)] for X in range(100)]


def Hash(Key):
    return Key % 100


def InsertData(RecordData):
    HashValue = Hash(RecordData.Key)
    for X in range(10):
        if HashTable[HashValue][X].Key == -1:
            HashTable[HashValue][X] = RecordData
            return


def ReadData():
    try:
        with open('HashTableData.txt') as File:
            for Line in File:
                Data = Line.rstrip('\r\n').split(',')
                InsertData(Record(int(Data[0]), Data[1]))
    except OSError:
        print('File not found')


def GetRecord(Key):
    HashValue = Hash(Key)
    for X in range(10):
        if HashTable[HashValue][X].Key == Key:
            return HashTable[HashValue][X].Data
    return 'Not found'


if __name__ == '__main__':
    InitialiseHashTable()
    ReadData()
    for X in range(5):
        Key = int(input('Enter key field: '))
        print(GetRecord(Key))
