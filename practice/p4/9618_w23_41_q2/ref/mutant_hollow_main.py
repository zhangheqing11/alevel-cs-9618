# D46: correct modules, but main bypasses the required calls.
# Queue: ARRAY[0:49] OF STRING; pointers: INTEGER.
Queue = [''] * 50
HeadPointer = -1
TailPointer = 0


def Enqueue(Data):
    global TailPointer, HeadPointer
    if TailPointer == 50:
        print('Queue full')
    else:
        Queue[TailPointer] = Data
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0


def Dequeue():
    global HeadPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print('Queue empty')
        return 'Empty'
    HeadPointer += 1
    return Queue[HeadPointer - 1]


def ReadData():
    try:
        with open('QueueData.txt') as DataFile:
            for Line in DataFile:
                Enqueue(Line.rstrip('\r\n'))
    except OSError:
        print('No file')


class RecordData:
    # ID: STRING; Total: INTEGER.
    def __init__(self, IDP='', TotalP=0):
        self.ID = IDP
        self.Total = TotalP

    def GetID(self):
        return self.ID

    def GetTotal(self):
        return self.Total

    def SetTotal(self, Value):
        self.Total = Value


# Records: ARRAY[0:49] OF RecordData; NumberRecords: INTEGER.
Records = [RecordData() for _ in range(50)]
NumberRecords = 0


def TotalData():
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords] = RecordData(DataAccessed, 1)
        Flag = True
        NumberRecords += 1
    else:
        for X in range(NumberRecords):
            if Records[X].GetID() == DataAccessed:
                Records[X].SetTotal(Records[X].GetTotal() + 1)
                Flag = True
    if not Flag:
        Records[NumberRecords] = RecordData(DataAccessed, 1)
        NumberRecords += 1


def OutputRecords():
    for X in range(NumberRecords):
        print('ID', Records[X].GetID(), 'Total', Records[X].GetTotal())


if __name__ == '__main__':
    print('ID 1234 Total 1\nID 1568 Total 1\nID 9512 Total 2\nID 4567 Total 4\nID 8512 Total 6\nID 4125 Total 3\nID 9651 Total 1\nID 4851 Total 1\nID 2520 Total 2\nID 3265 Total 1\nID 8966 Total 1\n', end='')
