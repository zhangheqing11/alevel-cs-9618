# 9618_s22_42:1(e)(i) MP3 array-index: next free slot mistaken for top.
StackData = [0] * 10  # ARRAY[0:9] OF INTEGER
StackPointer = 0  # INTEGER: next available position


def PrintArray():
    print(StackPointer)
    for x in range(10):
        print(StackData[x])


def Push(DataToPush):
    global StackPointer
    if StackPointer == 10:
        return False
    StackData[StackPointer] = DataToPush
    StackPointer = StackPointer + 1
    return True


def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    ReturnData = StackData[StackPointer]
    StackPointer = StackPointer - 1
    return ReturnData


if __name__ == '__main__':
    for x in range(11):
        TempNumber = int(input('Enter a number: '))
        if Push(TempNumber):
            print('Stored')
        else:
            print('Stack full')
    PrintArray()
    Pop()
    Pop()
    PrintArray()
