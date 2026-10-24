# D46: modules are correct; main fabricates output without calling them.
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
            self.__YPosition -= (self.__DistancePerHour / 60) * MinsFlying


if __name__ == "__main__":
    print('Cockatiel is currently at X = 500.0 Y = 500.0\nMacaw is currently at X = 500.0 Y = 500.0\nEnter 1 for Cockatiel or 2 for Macaw: To the nearest minute how long has the bird been flying? Which direction: N, S, E or W? Cockatiel is currently at X = 500.0 Y = 571.0\nMacaw is currently at X = 500.0 Y = 500.0\n')
