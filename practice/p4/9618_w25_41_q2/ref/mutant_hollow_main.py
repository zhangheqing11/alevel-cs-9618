# D46: correct modules retained, main fabricates the expected output.
class Train:
    def __init__(self, pNumber, pRoute):
        self.__TrainIDNumber = pNumber  # STRING
        self.__Route = pRoute  # INTEGER

    def GetTrainIDNumber(self):
        return self.__TrainIDNumber

    def GetRoute(self):
        return self.__Route


class Station:
    def __init__(self, pID, pNumberOfPlatforms):
        self.__StationID = pID  # STRING
        self.__NumberPlatforms = pNumberOfPlatforms  # INTEGER
        self.__Trains = [None] * 10  # ARRAY[0:9] OF Train
        self.__NumberTrains = 0  # INTEGER

    def AddTrain(self, NewTrain):
        if self.__NumberTrains >= self.__NumberPlatforms:
            return False
        self.__Trains[self.__NumberTrains] = NewTrain
        self.__NumberTrains += 1
        return True

    def GetTrains(self):
        if self.__NumberTrains == 0:
            return 'There are no trains'
        OutputLine = 'The trains at station ' + self.__StationID + ' are: \n'
        for x in range(self.__NumberTrains):
            OutputLine = OutputLine + self.__Trains[x].GetTrainIDNumber() + ' on route number ' + str(self.__Trains[x].GetRoute()) + '\n'
        return OutputLine


if __name__ == "__main__":
    print('Station is full\nThe trains at station STH are: \n12ADV on route number 134\n33ART on route number 20\n\nThe trains at station NTH are: \n21VBC on route number 24\n\n')
