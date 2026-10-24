# 9618_w25_42:3(b) MP4-MP6; binary-tree: left/right comparison reversed.
# TreeArray: ARRAY[0:49, 0:2] OF INTEGER (left, data, right).
TreeArray = [[-1, -1, -1] for _ in range(50)]
# RootPointer, FreeNode: INTEGER.
RootPointer = -1
FreeNode = 0


def AddNode(NodeData):
    global FreeNode, RootPointer
    if FreeNode <= 49:
        TreeArray[FreeNode] = [-1, NodeData, -1]
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData > TreeArray[CurrentNode][1]:
                    if TreeArray[CurrentNode][0] == -1:
                        TreeArray[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = TreeArray[CurrentNode][0]
                else:
                    if TreeArray[CurrentNode][2] == -1:
                        TreeArray[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = TreeArray[CurrentNode][2]
        FreeNode += 1
    else:
        print('The tree is full')


def WriteAllToFile():
    try:
        with open('Tree.txt', 'w') as File:
            for X in range(50):
                Line = str(TreeArray[X][0]) + ',' + str(TreeArray[X][1]) + ',' + str(TreeArray[X][2])
                File.write(Line + '\n')
    except OSError:
        print('Cannot write to file')


if __name__ == '__main__':
    try:
        with open('TreeData.txt') as File:
            for Line in File:
                AddNode(int(Line.strip()))
    except OSError:
        print('Error cannot open file')
    WriteAllToFile()
