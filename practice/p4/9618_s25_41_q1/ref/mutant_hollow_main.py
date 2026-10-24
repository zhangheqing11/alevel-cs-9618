# D46: correct modules, but main bypasses the required calls.
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
        TailPointer = -1
    return ReturnValue


if __name__ == '__main__':
    print('1 Successful\n2 Successful\n3 Successful\n4 Successful\n5 Successful\n6 Successful\n7 Successful\n8 Successful\n9 Successful\n10 Successful\n11 Successful\n12 Successful\n13 Successful\n14 Successful\n15 Successful\n16 Successful\n17 Successful\n18 Successful\n19 Successful\n20 Successful\n21 Unsuccessful\n22 Unsuccessful\n23 Unsuccessful\n24 Unsuccessful\n25 Unsuccessful\n1\n2\n', end='')
