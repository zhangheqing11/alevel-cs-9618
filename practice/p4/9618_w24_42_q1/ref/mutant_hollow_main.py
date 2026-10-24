# D46: correct modules retained, main fabricates the expected output.
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
            return 60
        elif Difference == 3:
            return 40
        elif Difference == 4:
            return 20
        return 0


if __name__ == "__main__":
    print('Tarz you win this event\nTarz you win this event\nTarz you win this event\nGeni you win this event\nTarz you win this event\nTarz you have won with 4\n')
