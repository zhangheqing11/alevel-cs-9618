# 9618_s25_42:1(e) MP6 operator-precedence: XOR mistaken for exponentiation.
Stack = ['-1'] * 20  # ARRAY[0:19] OF STRING
TopOfStack = -1  # INTEGER


def Push(Data):
    global TopOfStack
    if TopOfStack == 19:
        return -1
    TopOfStack += 1
    Stack[TopOfStack] = Data
    return 1


def Pop():
    global TopOfStack
    if TopOfStack == -1:
        return '-1'
    ReturnValue = Stack[TopOfStack]
    TopOfStack -= 1
    return ReturnValue


def ReadData(FileName):
    try:
        File = open(FileName, 'r')
        for Line in File:
            ReturnValue = Push(Line.strip())
            if ReturnValue == -1:
                print('Stack full')
        File.close()
    except OSError:
        print('Cannot open file')


def Calculate():
    Total = int(Pop())
    Return = ''
    LastOperator = ''
    Operator = True
    while Return != '-1':
        Return = Pop()
        if not Operator:
            Data = int(Return)
            if LastOperator == '+':
                Total = Total + Data
            elif LastOperator == '-':
                Total = Total - Data
            elif LastOperator == '*':
                Total = Total * Data
            elif LastOperator == '/':
                Total = Total / Data
            elif LastOperator == '^':
                Total = Total ^ Data
            Operator = True
        else:
            LastOperator = Return
            Operator = False
    return Total


if __name__ == '__main__':
    FileName = input('Enter the filename: ')
    ReadData(FileName)
    ReturnValue = Calculate()
    print(ReturnValue)
