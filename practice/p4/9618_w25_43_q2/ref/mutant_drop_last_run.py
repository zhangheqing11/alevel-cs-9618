# 9618_w25_43:2(e) MP3, MP6; loop-to-eof: MS example drops final singleton.
# Queue: ARRAY[0:99] OF STRING.
Queue = [''] * 100
# QueueHead, QueueTail, NumberItems: INTEGER; tail points to last occupied cell.
QueueHead = -1
QueueTail = -1
NumberItems = 0
NewString = ''  # STRING


def Enqueue(TheData):
    global QueueHead, QueueTail, NumberItems
    if QueueTail >= 99:
        return False
    Queue[QueueTail + 1] = TheData
    QueueTail += 1
    NumberItems += 1
    if QueueHead == -1:
        QueueHead = 0
    return True


def Dequeue():
    global QueueHead, NumberItems
    if NumberItems == 0:
        return 'False'
    ReturnData = Queue[QueueHead]
    QueueHead += 1
    NumberItems -= 1
    return ReturnData


def ReadData():
    try:
        with open('BinaryData.txt') as TheFile:
            for Line in TheFile:
                ReturnValue = Enqueue(Line.rstrip('\r\n'))
                if ReturnValue is False:
                    break
    except OSError:
        print('No file found')


def Compress():
    global NewString
    First = Dequeue()
    NewString = ''
    while NumberItems > 0 and First != 'False':
        Count = 1
        NextChar = Dequeue()
        while NextChar == First:
            Count += 1
            First = NextChar
            NextChar = Dequeue()
        NewString = NewString + First + str(Count)
        First = NextChar


if __name__ == '__main__':
    ReadData()
    Compress()
    print(NewString)
