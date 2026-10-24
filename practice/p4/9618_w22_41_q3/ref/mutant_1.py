# 9618_w22_41:3(c) MP1 binary-tree: left branch incorrectly follows right pointer.
ArrayNodes = []  # ARRAY[0:19, 0:2] OF INTEGER
for x in range(20):
    ArrayNodes.append([-1, -1, -1])

ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
FreeNode = 6  # INTEGER
RootPointer = 0  # INTEGER


def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)


def PostOrder(RootNode):
    if RootNode[0] != -1:
        PostOrder(ArrayNodes[RootNode[0]])
    if RootNode[2] != -1:
        PostOrder(ArrayNodes[RootNode[2]])
    print(str(RootNode[1]))


if __name__ == '__main__':
    ReturnValue = SearchValue(RootPointer, 15)
    if ReturnValue == -1:
        print('Not found')
    else:
        print('Found at ' + str(ReturnValue))
    PostOrder(ArrayNodes[RootPointer])
