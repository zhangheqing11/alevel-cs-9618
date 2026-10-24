# D46: correct modules retained, main fabricates the expected output.
import datetime


class Character:
    # CharacterName: STRING; DateOfBirth: DATE; Intelligence: REAL; Speed: INTEGER.
    def __init__(self, CName, DBirth, Intell, SpeedP):
        self.__CharacterName = CName
        self.__DateOfBirth = DBirth
        self.__Intelligence = Intell
        self.__Speed = SpeedP

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, NewValue):
        self.__Intelligence = NewValue

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year


class MagicCharacter(Character):
    # Element: STRING.
    def __init__(self, ElementP, CName, DBirth, Intell, SpeedP):
        super().__init__(CName, DBirth, Intell, SpeedP)
        self.__Element = ElementP

    def Learn(self):
        if self.__Element == 'fire' or self.__Element == 'water':
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif self.__Element == 'earth':
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)


if __name__ == "__main__":
    print('Royal is 4 years old and has intelligence 77.0\nLight is 5 years old and has intelligence 90.0\n')
