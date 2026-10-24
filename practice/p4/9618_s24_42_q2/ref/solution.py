class Node:
    # LeftPointer, Data, RightPointer : INTEGER.
    def __init__(self, PData):
        self.__LeftPointer = -1
        self.__Data = PData
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer

    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    def SetLeft(self, NewLeft):
        self.__LeftPointer = NewLeft

    def SetRight(self, NewRight):
        self.__RightPointer = NewRight

    def SetData(self, NewData):
        self.__Data = NewData


class TreeClass:
    # Tree : ARRAY[0:19] OF Node; FirstNode, NumberNodes : INTEGER.
    def __init__(self):
        self.__Tree = [Node(-1) for x in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0

    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[0] = NewNode
            self.__FirstNode = 0
            self.__NumberNodes += 1
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            NodeAccess = self.__FirstNode
            Direction = ""
            while NodeAccess != -1:
                Previous = NodeAccess
                if NewNode.GetData() < self.__Tree[NodeAccess].GetData():
                    NodeAccess = self.__Tree[NodeAccess].GetLeft()
                    Direction = "left"
                else:
                    NodeAccess = self.__Tree[NodeAccess].GetRight()
                    Direction = "right"
            if Direction == "left":
                self.__Tree[Previous].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[Previous].SetRight(self.__NumberNodes)
            self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for x in range(self.__NumberNodes):
                print(self.__Tree[x].GetLeft(),self.__Tree[x].GetData(),self.__Tree[x].GetRight())


if __name__ == "__main__":
    TheTree = TreeClass()
    for Data in [10,11,5,1,20,7,15]:
        TheTree.InsertNode(Node(Data))
    TheTree.OutputTree()
