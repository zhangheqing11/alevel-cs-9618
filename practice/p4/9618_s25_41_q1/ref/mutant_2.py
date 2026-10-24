# 9618_s25_41:1(d) MP6 queue-array: failed reset of tail on empty.
Queue = [-1 for x in range(20)]  # ARRAY[0:19] OF INTEGER
HeadPointer = -1  # INTEGER
TailPointer = -1  # INTEGER
NumberItems = 0  # INTEGER


def Enqueue(InputData):
    global HeadPointer, TailPointer, NumberItems
    if NumberItems >= 20:
        return False
    if TailPointer <= -1:
        TailPointer = 0
        HeadPointer = 0
    else:
        TailPointer = TailPointer + 1
        if TailPointer == 20:
            TailPointer = 0
    Queue[TailPointer] = InputData
    NumberItems += 1
    return True


def Dequeue():
    global HeadPointer, TailPointer, NumberItems
    if NumberItems <= 0:
        return -1
    ReturnValue = Queue[HeadPointer]
    HeadPointer += 1
    if HeadPointer >= 20:
        HeadPointer = 0
    NumberItems -= 1
    if NumberItems == 0:
        HeadPointer = -1
        TailPointer = 0
    return ReturnValue


if __name__ == '__main__':
    for X in range(1, 26):
        ReturnValue = Enqueue(X)
        if ReturnValue:
            print(X, 'Successful')
        else:
            print(X, 'Unsuccessful')
    NextValue = Dequeue()
    print(NextValue)
    NextValue = Dequeue()
    print(NextValue)
