# 9618_s25_43:1(d) MP3 type-conversion: queue data left as strings.
Queue = [-1] * 50  # ARRAY[0:49] OF INTEGER
HeadPointer = -1  # INTEGER
TailPointer = -1  # INTEGER


def Enqueue(Data):
    global TailPointer, HeadPointer
    if TailPointer < 49:
        TailPointer = TailPointer + 1
        Queue[TailPointer] = str(Data)
        if HeadPointer == -1:
            HeadPointer = 0
        return True
    return False


def Dequeue():
    global HeadPointer
    if HeadPointer > -1 and HeadPointer <= TailPointer:
        ReturnValue = Queue[HeadPointer]
        HeadPointer = HeadPointer + 1
        return ReturnValue
    return -1


def CreateQueue():
    try:
        File = open('QueueData.txt', 'r')
        for Line in File:
            ReturnValue = Enqueue(int(Line))
            if not ReturnValue:
                print('Queue full')
        File.close()
    except OSError:
        print('Cannot open or read file')


if __name__ == '__main__':
    CreateQueue()
    Total = 0
    ReturnValue = 0
    while ReturnValue > -1:
        ReturnValue = Dequeue()
        if ReturnValue != -1:
            Total = Total + ReturnValue
    print('The total is', Total)
