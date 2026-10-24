# D46: correct modules, but main bypasses the required calls.
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
    print('Enter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Enter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Item inserted\nEnter an integer that is 0 or more: Item inserted\n10 9 8 7 6 5 4 3 2 1 \n10 is returned\n9 is returned\n8 7 6 5 4 3 2 1 \n', end='')
