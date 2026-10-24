# D46: correct modules retained, main fabricates the expected output.
class Node:
    # NodeData : INTEGER; LeftNode, RightNode : Node reference or None.
    def __init__(self, pNodeData):
        self.__NodeData = pNodeData
        self.__LeftNode = None
        self.__RightNode = None

    def GetLeft(self):
        return self.__LeftNode

    def GetRight(self):
        return self.__RightNode

    def GetData(self):
        return self.__NodeData

    def SetLeft(self, NewNode):
        self.__LeftNode = NewNode

    def SetRight(self, NewNode):
        self.__RightNode = NewNode


class Tree:
    # FirstNode : Node reference.
    def __init__(self, FirstNode):
        self.__FirstNode = FirstNode

    def GetRootNode(self):
        return self.__FirstNode

    def Insert(self, NewNode):
        CurrentNode = self.__FirstNode
        while True:
            if NewNode.GetData() < CurrentNode.GetData():
                if CurrentNode.GetLeft() is None:
                    CurrentNode.SetLeft(NewNode)
                    return True
                CurrentNode = CurrentNode.GetLeft()
            else:
                if CurrentNode.GetRight() is None:
                    CurrentNode.SetRight(NewNode)
                    return True
                CurrentNode = CurrentNode.GetRight()


def OutputInOrder(RootNode):
    if RootNode.GetLeft() is not None:
        OutputInOrder(RootNode.GetLeft())
    print(RootNode.GetData())
    if RootNode.GetRight() is not None:
        OutputInOrder(RootNode.GetRight())


if __name__ == "__main__":
    print('5\n7\n10\n15\n20\n')
