# 9618_s22_41:3(b) MP1 queue-array: off-by-one tail wrap.
QueueArray = [''] * 10  # ARRAY[0:9] OF STRING
QueueHeadPointer = 0  # INTEGER
QueueTailPointer = 0  # INTEGER
NumberOfItems = 0  # INTEGER


def Enqueue(Queue, Head, Tail, NumItems, InputData):
    if NumItems == 10:
        return False, Queue, Head, Tail, NumItems
    Queue[Tail] = InputData
    if Tail > 9:
        Tail = 0
    else:
        Tail = Tail + 1
    NumItems = NumItems + 1
    return True, Queue, Head, Tail, NumItems


def Dequeue(Queue, Head, Tail, NumItems):
    if NumItems == 0:
        return 'FALSE', Queue, Head, Tail, NumItems
    ReturnValue = Queue[Head]
    Head = Head + 1
    if Head > 9:
        Head = 0
    NumItems = NumItems - 1
    return ReturnValue, Queue, Head, Tail, NumItems


if __name__ == '__main__':
    for x in range(11):
        InputString = input('Enter a string: ')
        ReturnValue, QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems = Enqueue(
            QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems, InputString)
        if ReturnValue:
            print('Successful')
        else:
            print('Unsuccessful')
    for x in range(2):
        ReturnValue, QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems = Dequeue(
            QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems)
        print(ReturnValue)
