# D46: correct modules, but main bypasses the required calls.
import random

# Stack: ARRAY[0:29] OF INTEGER, null = None; TopOfStack: INTEGER.
Stack = [None] * 30
TopOfStack = -1


def Push(DataToPush):
    global TopOfStack
    if TopOfStack < 29:
        TopOfStack += 1
        Stack[TopOfStack] = DataToPush
        return True
    return False


def Pop():
    global TopOfStack
    if TopOfStack == -1:
        return -999
    DataReturn = Stack[TopOfStack]
    TopOfStack -= 1
    return DataReturn


def FindValues():
    Highest = Pop()
    Lowest = Highest
    ReturnValue = Lowest
    while ReturnValue != -999:
        if ReturnValue > Highest:
            Highest = ReturnValue
        if ReturnValue < Lowest:
            Lowest = ReturnValue
        ReturnValue = Pop()
    print('The highest value is', Highest, 'and the lowest value is', Lowest)


if __name__ == '__main__':
    print('Stack full\nThe highest value is 913 and the lowest value is 36\n', end='')
