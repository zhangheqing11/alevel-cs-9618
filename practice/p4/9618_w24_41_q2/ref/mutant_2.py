# 9618_w24_41:2(e)(ii) MP2 max-min: first winner never initialised.
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


if __name__ == '__main__':
    Horses = [Horse('Beauty', 150, 72), Horse('Jet', 160, 65)]  # ARRAY[0:1] OF Horse
    print(Horses[0].GetName())
    print(Horses[1].GetName())
    Course = [None] * 4  # ARRAY[0:3] OF Fence
    for x in range(4):
        Height = int(input('Enter height in cm: '))
        while Height < 70 or Height > 180:
            Height = int(input('Enter height between 70 and 180: '))
        Risk = int(input('Enter risk between 1 and 5: '))
        while Risk < 1 or Risk > 5:
            Risk = int(input('Enter risk between 1 and 5: '))
        Course[x] = Fence(Height, Risk)
    AverageSuccess = [0.0] * 2  # ARRAY[0:1] OF REAL
    for y in range(2):
        Total = 0
        for x in range(4):
            Chance = Horses[y].Success(Course[x].GetHeight(), Course[x].GetRisk())
            print(Horses[y].GetName(), 'Fence', x + 1, 'chance of success is', Chance, '%')
            Total = Total + Chance
        AverageSuccess[y] = Total / 4
        print(Horses[y].GetName(), 'average success rate is', AverageSuccess[y], '%')
    Highest = AverageSuccess[0]
    Winner = -1
    for x in range(1, 2):
        if Highest < AverageSuccess[x]:
            Winner = x
            Highest = AverageSuccess[x]
    print(Horses[Winner].GetName(), 'has the highest average chance of success')
