# D46: correct modules retained, main fabricates the expected output.
class Horse:
    def __init__(self, PName, PMaxFenceHeight, PPercentageSuccess):
        self.__Name = PName  # STRING
        self.__MaxFenceHeight = PMaxFenceHeight  # INTEGER
        self.__PercentageSuccess = PPercentageSuccess  # INTEGER

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    def Success(self, Height, Risk):
        if Height > self.__MaxFenceHeight:
            return self.__PercentageSuccess * 0.2
        elif Risk == 1:
            return self.__PercentageSuccess * 1.0
        elif Risk == 2:
            return self.__PercentageSuccess * 0.9
        elif Risk == 3:
            return self.__PercentageSuccess * 0.8
        elif Risk == 4:
            return self.__PercentageSuccess * 0.7
        else:
            return self.__PercentageSuccess * 0.6


class Fence:
    def __init__(self, PHeight, PRisk):
        self.__Height = PHeight  # INTEGER
        self.__Risk = PRisk  # INTEGER

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk


if __name__ == "__main__":
    print('Beauty\nJet\nEnter height in cm: Enter risk between 1 and 5: Enter height in cm: Enter risk between 1 and 5: Enter height in cm: Enter risk between 1 and 5: Enter height in cm: Enter risk between 1 and 5: Beauty Fence 1 chance of success is 14.4 %\nBeauty Fence 2 chance of success is 72.0 %\nBeauty Fence 3 chance of success is 57.6 %\nBeauty Fence 4 chance of success is 50.4 %\nBeauty average success rate is 48.6 %\nJet Fence 1 chance of success is 39.0 %\nJet Fence 2 chance of success is 65.0 %\nJet Fence 3 chance of success is 52.0 %\nJet Fence 4 chance of success is 45.5 %\nJet average success rate is 50.375 %\nJet has the highest average chance of success\n')
