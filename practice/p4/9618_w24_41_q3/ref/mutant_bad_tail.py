# 9618_w24_41:3(a) MP1; linked-list: free list fails to terminate.
# LinkedList: ARRAY[0:19, 0:1] OF INTEGER (data, next pointer).
LinkedList = [[-1, X + 1] for X in range(20)]
LinkedList[19][1] = 0
# FirstNode, FirstEmpty: INTEGER.
FirstNode = -1
FirstEmpty = 0


def InsertData():
    global FirstNode, FirstEmpty
    for _ in range(5):
        if FirstEmpty == -1:
            return
        NextEmpty = LinkedList[FirstEmpty][1]
        LinkedList[FirstEmpty][0] = int(input('Value: '))
        LinkedList[FirstEmpty][1] = FirstNode
        FirstNode = FirstEmpty
        FirstEmpty = NextEmpty


def OutputLinkedList():
    CurrentPointer = FirstNode
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]


def RemoveData(ItemToRemove):
    global FirstNode, FirstEmpty
    if LinkedList[FirstNode][0] == ItemToRemove:
        CurrentPointer = FirstNode
        FirstNode = LinkedList[FirstNode][1]
    else:
        CurrentPointer = FirstNode
        PreviousNode = -1
        while LinkedList[CurrentPointer][0] != ItemToRemove:
            PreviousNode = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer][1]
        LinkedList[PreviousNode][1] = LinkedList[CurrentPointer][1]
    LinkedList[CurrentPointer][1] = FirstEmpty
    FirstEmpty = CurrentPointer


if __name__ == '__main__':
    InsertData()
    OutputLinkedList()
    RemoveData(5)
    print('After')
    OutputLinkedList()
