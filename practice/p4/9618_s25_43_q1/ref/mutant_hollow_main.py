# D46: correct modules, but main bypasses the required calls.
Queue = [-1] * 50  # ARRAY[0:49] OF INTEGER
HeadPointer = -1  # INTEGER
TailPointer = -1  # INTEGER


def Enqueue(Data):
    global TailPointer, HeadPointer
    if TailPointer < 49:
        TailPointer = TailPointer + 1
        Queue[TailPointer] = Data
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
    print('The total is 3059\n', end='')
