# 9618_s24_41:3(b) MP3 array-index: append beyond preallocated slots.
QueueData = [''] * 20  # ARRAY[0:19] OF STRING
QueueHead = -1  # INTEGER
QueueTail = -1  # INTEGER


def Enqueue(DataToInsert):
    global QueueHead, QueueTail
    if QueueTail == 19:
        return False
    if QueueHead == -1:
        QueueHead = 0
    QueueTail = QueueTail + 1
    QueueData.append(DataToInsert)
    return True


def Dequeue():
    global QueueHead
    if QueueHead < 0 or QueueHead > QueueTail:
        return 'false'
    QueueHead = QueueHead + 1
    return QueueData[QueueHead - 1]


def StoreItems():
    Count = 0
    for X in range(10):
        Data = input('Enter data: ')
        Total = (int(Data[0]) + int(Data[1]) * 3 + int(Data[2])
                 + int(Data[3]) * 3 + int(Data[4]) + int(Data[5]) * 3)
        Total = Total // 10
        CheckDigit = 'X' if Total == 10 else str(Total)
        if CheckDigit == Data[6]:
            Result = Enqueue(Data[:6])
            if Result:
                print('Inserted item')
            else:
                print('Queue full')
        else:
            Count = Count + 1
    print('There were', Count, 'invalid items')


if __name__ == '__main__':
    StoreItems()
    Value = Dequeue()
    if Value == 'false':
        print('No data items')
    else:
        print('Item code', Value)
