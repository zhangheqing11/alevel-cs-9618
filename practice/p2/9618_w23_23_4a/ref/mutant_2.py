# 9618_w23_23:4(a) MP5: random-numbers
import random

def RandList():
    BaseNum=0
    for Count in range(25):
        ThisNum=BaseNum+random.randrange(10)
        print(ThisNum)
        BaseNum+=0
