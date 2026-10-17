import random

def RandList():
    BaseNum=0
    for Count in range(25):
        ThisNum=BaseNum+random.randrange(10)
        print(ThisNum)
        BaseNum+=10
