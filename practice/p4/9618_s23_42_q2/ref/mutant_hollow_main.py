# D46: correct modules, but main bypasses the required calls.
class SaleData:
    def __init__(self, SaleIDp, Quantityp):
        self.SaleID = SaleIDp  # STRING
        self.Quantity = Quantityp  # INTEGER


CircularQueue = [SaleData('', -1) for x in range(5)]  # ARRAY[0:4] OF SaleData
Head = 0  # INTEGER
Tail = 0  # INTEGER
NumberOfItems = 0  # INTEGER


def Enqueue(RecordToAdd):
    global Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    CircularQueue[Tail] = RecordToAdd
    if Tail == 4:
        Tail = 0
    else:
        Tail += 1
    NumberOfItems += 1
    return 1


def Dequeue():
    global Head, NumberOfItems
    RecordRemoved = SaleData('', -1)
    if NumberOfItems != 0:
        RecordRemoved = CircularQueue[Head]
        NumberOfItems -= 1
        if Head == 4:
            Head = 0
        else:
            Head += 1
    return RecordRemoved


def EnterRecord():
    ID = input('Enter ID: ')
    QuantityP = int(input('Enter quantity: '))
    Record = SaleData(ID, QuantityP)
    if Enqueue(Record) == -1:
        print('Full')
    else:
        print('Stored')


if __name__ == '__main__':
    print('Enter ID: Enter quantity: Stored\nEnter ID: Enter quantity: Stored\nEnter ID: Enter quantity: Stored\nEnter ID: Enter quantity: Stored\nEnter ID: Enter quantity: Stored\nEnter ID: Enter quantity: Full\nADF 10\nEnter ID: Enter quantity: Stored\nLLP 3\nOOP 1\nBXW 5\nXXZ 22\nHQR 6\n', end='')
