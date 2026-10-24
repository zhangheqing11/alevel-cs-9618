# 9618_w25_42:1(a)(iv) MP4 nested-if: south has wrong sign.
class Bird:
    def __init__(self, pDistancePerHour, pSpecies):
        self.__Species = pSpecies  # STRING
        self.__DistancePerHour = pDistancePerHour  # REAL
        self.__XPosition = 500.0  # REAL
        self.__YPosition = 500.0  # REAL

    def GetSpecies(self):
        return self.__Species

    def GetPosition(self):
        ReturnValue = 'X = ' + str(self.__XPosition) + ' Y = ' + str(self.__YPosition)
        return ReturnValue

    def Move(self, Direction, MinsFlying):
        if Direction == 'E':
            self.__XPosition += (self.__DistancePerHour / 60) * MinsFlying
        elif Direction == 'W':
            self.__XPosition -= (self.__DistancePerHour / 60) * MinsFlying
        elif Direction == 'N':
            self.__YPosition += (self.__DistancePerHour / 60) * MinsFlying
        elif Direction == 'S':
            self.__YPosition += (self.__DistancePerHour / 60) * MinsFlying


if __name__ == '__main__':
    FirstBird = Bird(71.0, 'Cockatiel')
    SecondBird = Bird(56.0, 'Macaw')
    print(FirstBird.GetSpecies(), 'is currently at', FirstBird.GetPosition())
    print(SecondBird.GetSpecies(), 'is currently at', SecondBird.GetPosition())
    Choice = int(input('Enter 1 for Cockatiel or 2 for Macaw: '))
    while Choice != 1 and Choice != 2:
        Choice = int(input('Enter 1 or 2: '))
    Time = int(input('To the nearest minute how long has the bird been flying? '))
    while Time < 0 or Time > 500:
        Time = int(input('Enter time between 0 and 500: '))
    Direction = input('Which direction: N, S, E or W? ').upper()
    while Direction != 'N' and Direction != 'S' and Direction != 'E' and Direction != 'W':
        Direction = input('Enter N, S, E or W: ').upper()
    if Choice == 1:
        FirstBird.Move(Direction, Time)
    else:
        SecondBird.Move(Direction, Time)
    print(FirstBird.GetSpecies(), 'is currently at', FirstBird.GetPosition())
    print(SecondBird.GetSpecies(), 'is currently at', SecondBird.GetPosition())
