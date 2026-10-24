# 9618_s25_43:3(b)(iv) MP4: linked-list.
class Node:
    # TheData : INTEGER; NextNode : Node reference or None.
    def __init__(self, NodeData):
        self.__TheData = NodeData
        self.__NextNode = None

    def GetData(self):
        return self.__TheData

    def GetNextNode(self):
        return self.__NextNode

    def SetNextNode(self, pNextNode):
        self.__NextNode = pNextNode


class LinkedList:
    # HeadNode : Node reference or None.
    def __init__(self):
        self.__HeadNode = None

    def InsertNode(self, NodeData):
        TheNode = Node(NodeData)
        TheNode.SetNextNode(self.__HeadNode)
        self.__HeadNode = TheNode

    def Traverse(self):
        ReturnValue = ""
        CurrentNode = self.__HeadNode
        while CurrentNode is not None:
            ReturnValue = ReturnValue + str(CurrentNode.GetData()) + " "
            CurrentNode = CurrentNode.GetNextNode()
        return ReturnValue

    def RemoveNode(self, DataToRemove):
        if self.__HeadNode is None:
            return False
        if self.__HeadNode.GetData() == DataToRemove:
            self.__HeadNode = None
            return True
        CurrentNode = self.__HeadNode
        while CurrentNode.GetNextNode() is not None:
            NextNode = CurrentNode.GetNextNode()
            if NextNode.GetData() == DataToRemove:
                CurrentNode.SetNextNode(NextNode.GetNextNode())
                return True
            CurrentNode = NextNode
        return False


if __name__ == "__main__":
    CreateList = LinkedList()
    CreateList.InsertNode(10)
    CreateList.InsertNode(20)
    CreateList.InsertNode(30)
    CreateList.InsertNode(40)
    CreateList.InsertNode(50)
    ReturnValue1 = CreateList.Traverse()
    print(ReturnValue1)
    CreateList.RemoveNode(30)
    ReturnValue2 = CreateList.Traverse()
    print(ReturnValue2)
