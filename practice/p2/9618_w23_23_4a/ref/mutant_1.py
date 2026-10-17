# 9618_w23_23:4(a) MP3: loop-bounds
import random

def RandList():
    BaseNum=0
    for Count in range(24):
        ThisNum=BaseNum+random.randrange(10)
        print(ThisNum)
        BaseNum+=10
