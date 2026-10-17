# 9618_w24_22:6(a) MP3: relational-ops
import random
# Provided QP arrays; Python indices = QP - 1. Remaining sample slots unused.
Filling=['Cheese','Onion','Salmon','Anchovies','Peanut Butter']+['']*30
Bread=['White','Brown','Pitta']+['']*7
# RAND is the insert's random function, supplied for deterministic tests.
def RAND(Limit):
    return random.random()*Limit

def Special():
    while True:
        Index=int(RAND(35))
        if Filling[Index]!='':
            Filling1=Filling[Index]
            break
    while True:
        Index=int(RAND(35))
        if Filling[Index]!='' :
            Filling2=Filling[Index]
            break
    while True:
        Index=int(RAND(10))
        if Bread[Index]!='':
            break
    print('The daily special is '+Filling1+' and '+Filling2+' on '+Bread[Index]+' bread.')
