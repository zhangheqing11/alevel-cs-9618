import random

def RollDice(NoOfTimes):
    Sum=0
    for Count in range(NoOfTimes):
        RollValue=random.randint(1,6)
        print(RollValue)
        Sum+=RollValue
    return Sum/NoOfTimes
