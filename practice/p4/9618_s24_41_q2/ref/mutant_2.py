# 9618_s24_41:2(e)(ii) MP2: operator-precedence.
class Tree:
    # TreeName, Evergreen : STRING; HeightGrowth, MaxHeight, MaxWidth : INTEGER (private).
    def __init__(self, Name, HGrowth, MaxH, MaxW, PEvergreen):
        self.__TreeName = Name
        self.__HeightGrowth = HGrowth
        self.__MaxHeight = MaxH
        self.__MaxWidth = MaxW
        self.__Evergreen = PEvergreen

    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen


def ReadData():
    TreeObjects = []  # 9 Tree objects, appended from the file.
    try:
        with open("Trees.txt", "r") as File:
            for Line in File:
                Item = Line.rstrip("\r\n").split(",")
                TreeObjects.append(Tree(Item[0], int(Item[1]), int(Item[2]), int(Item[3]), Item[4]))
    except IOError:
        print("Invalid file")
    return TreeObjects


def PrintTrees(Item):
    Final = "does not lose its leaves."
    if Item.GetEvergreen() == "No":
        Final = "loses its leaves each year."
    print(Item.GetTreeName(), "has a maximum height", Item.GetMaxHeight(),
          "a maximum width", Item.GetMaxWidth(), "and grows", Item.GetGrowth(), "cm a year. It", Final)


def ChooseTree(Trees):
    Evergreen = input("Enter lose or keep: ")
    MaxHeight = int(input("Maximum height in cm: "))
    MaxWidth = int(input("Maximum width in cm: "))
    Keep = "Yes" if Evergreen.lower() == "keep" else "No"
    Options = []  # Tree objects meeting all requirements.
    for Item in Trees:
        if Item.GetMaxHeight() <= MaxHeight and Item.GetMaxWidth() <= MaxWidth and Item.GetEvergreen() == Keep:
            Options.append(Item)
            PrintTrees(Item)
    if len(Options) == 0:
        print("No suitable trees")
    else:
        Valid = False
        while not Valid:
            Choice = input("Enter the name of the tree you want: ")
            for Item in Options:
                if Item.GetTreeName() == Choice:
                    Valid = True
                    Start = int(input("Enter the starting height in cm: "))
                    Years = Item.GetMaxHeight() - Start / Item.GetGrowth()
                    print("Your tree should be full height in approximately", Years, "years")


if __name__ == "__main__":
    TreeObjects = ReadData()
    PrintTrees(TreeObjects[0])
    ChooseTree(TreeObjects)
