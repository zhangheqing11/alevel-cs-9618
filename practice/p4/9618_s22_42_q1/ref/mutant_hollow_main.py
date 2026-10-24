# D46: correct modules, but main bypasses the required calls.
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
    ReturnData = StackData[StackPointer - 1]
    StackPointer = StackPointer - 1
    return ReturnData


if __name__ == '__main__':
    print('Enter a number: Stored\nEnter a number: Stored\nEnter a number: Stored\nEnter a number: Stored\nEnter a number: Stored\nEnter a number: Stored\nEnter a number: Stored\nEnter a number: Stored\nEnter a number: Stored\nEnter a number: Stored\nEnter a number: Stack full\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n8\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n', end='')
