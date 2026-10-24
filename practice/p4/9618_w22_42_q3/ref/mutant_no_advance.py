# 9618_w22_42:3(b) MP4; queue-array: tail never advances.
# Queue: ARRAY[0:99] OF INTEGER; pointers: INTEGER.
Queue = [-1] * 100
HeadPointer = -1
TailPointer = 0


def Enqueue(Data):
    global HeadPointer, TailPointer
    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = Data
        TailPointer += 0
        return True
    return False


def RecursiveOutput(Start):
    if Start == HeadPointer:
        return Queue[Start]
    return Queue[Start] + RecursiveOutput(Start - 1)


if __name__ == '__main__':
    Success = True
    for Count in range(1, 21):
        if not Enqueue(Count):
            Success = False
    if Success:
        print('Successful')
    else:
        print('Unsuccessful')
    print(RecursiveOutput(TailPointer - 1))
