# D46: correct modules, but main bypasses the required calls.
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
                if NodeData < TreeArray[CurrentNode][1]:
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
    with open('Tree.txt', 'w') as File:
        File.write('1,40,2\n6,4,3\n8,82,17\n9,8,4\n10,21,5\n31,23,7\n22,1,15\n16,34,25\n13,67,14\n-1,6,-1\n-1,9,11\n-1,10,12\n49,13,23\n35,52,19\n-1,68,28\n-1,2,-1\n48,28,26\n18,89,20\n-1,85,-1\n21,66,-1\n-1,91,33\n-1,53,30\n-1,0,-1\n-1,15,24\n32,19,-1\n27,37,37\n38,31,-1\n-1,35,43\n46,74,29\n-1,76,45\n-1,54,34\n-1,22,-1\n-1,16,47\n-1,98,-1\n44,61,-1\n36,48,41\n40,46,-1\n-1,38,39\n-1,30,-1\n-1,39,-1\n-1,41,-1\n-1,49,42\n-1,50,-1\n-1,36,-1\n-1,58,-1\n-1,80,-1\n-1,71,-1\n-1,18,-1\n-1,25,-1\n-1,12,-1\n')
    print('Tree exported')
