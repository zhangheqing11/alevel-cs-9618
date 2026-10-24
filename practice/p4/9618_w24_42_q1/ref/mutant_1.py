# 9618_w24_42:1(d) MP4 nested-if: wrong difference-2 chance.
class EventItem:
    def __init__(self, pName, pType, pDifficulty):
        self.__EventName = pName  # STRING
        self.__Type = pType  # STRING
        self.__Difficulty = pDifficulty  # INTEGER

    def GetName(self):
        return self.__EventName

    def GetEventType(self):
        return self.__Type

    def GetDifficulty(self):
        return self.__Difficulty


class Character:
    def __init__(self, pName, pJump, pSwim, pRun, pDrive):
        self.__CharacterName = pName  # STRING
        self.__Jump = pJump  # INTEGER
        self.__Swim = pSwim  # INTEGER
        self.__Run = pRun  # INTEGER
        self.__Drive = pDrive  # INTEGER

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, Type, Difficulty):
        if Type == 'jump':
            Chance = self.__Jump
        elif Type == 'swim':
            Chance = self.__Swim
        elif Type == 'run':
            Chance = self.__Run
        else:
            Chance = self.__Drive
        if Chance >= Difficulty:
            return 100
        Difference = Difficulty - Chance
        if Difference == 1:
            return 80
        elif Difference == 2:
            return 40
        elif Difference == 3:
            return 40
        elif Difference == 4:
            return 20
        return 0


if __name__ == '__main__':
    Group = [EventItem('Bridge', 'jump', 3), EventItem('Water wade', 'swim', 4),
             EventItem('100 mile run', 'run', 5), EventItem('Gridlock', 'drive', 2),
             EventItem('Wall on wall', 'jump', 4)]  # ARRAY[0:4] OF EventItem
    P1 = Character('Tarz', 5, 3, 5, 1)
    P2 = Character('Geni', 2, 2, 3, 4)
    P1Points = 0
    P2Points = 0
    for x in range(5):
        P1EventScore = P1.CalculateScore(Group[x].GetEventType(), Group[x].GetDifficulty())
        P2EventScore = P2.CalculateScore(Group[x].GetEventType(), Group[x].GetDifficulty())
        if P1EventScore > P2EventScore:
            P1Points = P1Points + 1
            print(P1.GetName(), 'you win this event')
        elif P2EventScore > P1EventScore:
            P2Points = P2Points + 1
            print(P2.GetName(), 'you win this event')
        else:
            print('This event is a draw')
    if P1Points > P2Points:
        print(P1.GetName(), 'you have won with', P1Points)
    elif P2Points > P1Points:
        print(P2.GetName(), 'you have won with', P2Points)
    else:
        print("It's a draw")
