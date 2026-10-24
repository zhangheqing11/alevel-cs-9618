# 9618_s22_41:2(d) MP2: boolean-return.
class Balloon:
    # Health : INTEGER; Colour, DefenceItem : STRING (private).
    def __init__(self, PDefenceItem, PColour):
        self.__Health = 100
        self.__Colour = PColour
        self.__DefenceItem = PDefenceItem

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, Change):
        self.__Health = self.__Health + Change

    def CheckHealth(self):
        return self.__Health < 0


def Defend(MyBalloon):
    Strength = int(input("Enter the strength of opponent: "))
    MyBalloon.ChangeHealth(-Strength)
    print("You defended with", MyBalloon.GetDefenceItem())
    if MyBalloon.CheckHealth():
        print("Defence failed")
    else:
        print("Defence succeeded")
    return MyBalloon


if __name__ == "__main__":
    Method = input("Enter balloon defence method: ")
    Colour = input("Enter the balloon colour: ")
    Balloon1 = Balloon(Method, Colour)
    Balloon1 = Defend(Balloon1)
