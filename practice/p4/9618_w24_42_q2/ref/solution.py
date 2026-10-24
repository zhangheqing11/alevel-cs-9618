class Queue:
    # QueueArray: ARRAY[0:99] OF INTEGER.
    # HeadPointer, TailPointer: INTEGER.
    def __init__(self):
        self.QueueArray = [-1] * 100
        self.HeadPointer = -1
        self.TailPointer = 0


def Enqueue(AQueue, TheData):
    if AQueue.HeadPointer == -1:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.HeadPointer = 0
        AQueue.TailPointer += 1
        return AQueue, 1
    if AQueue.TailPointer > 99:
        return AQueue, -1
    AQueue.QueueArray[AQueue.TailPointer] = TheData
    AQueue.TailPointer += 1
    return AQueue, 1


def ReturnAllData(TheQueue):
    Temp = ''
    for X in range(TheQueue.HeadPointer, TheQueue.TailPointer):
        Temp += str(TheQueue.QueueArray[X]) + ' '
    return Temp


def Dequeue(AQueue):
    if AQueue.HeadPointer == -1 or AQueue.HeadPointer == AQueue.TailPointer:
        return AQueue, -1
    Temp = AQueue.QueueArray[AQueue.HeadPointer]
    AQueue.HeadPointer += 1
    return AQueue, Temp


if __name__ == '__main__':
    TheQueue = Queue()
    for X in range(10):
        Continue = True
        while Continue:
            DataInput = int(input('Enter an integer that is 0 or more: '))
            if DataInput >= 0:
                Continue = False
        TheQueue, ReturnValue = Enqueue(TheQueue, DataInput)
        if ReturnValue == -1:
            print('Queue full')
        else:
            print('Item inserted')
    print(ReturnAllData(TheQueue))
    for X in range(2):
        TheQueue, ReturnValue = Dequeue(TheQueue)
        if ReturnValue == -1:
            print('Queue empty')
        else:
            print(ReturnValue, 'is returned')
    print(ReturnAllData(TheQueue))
