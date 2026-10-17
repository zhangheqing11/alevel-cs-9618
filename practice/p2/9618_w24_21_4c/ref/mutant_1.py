# 9618_w24_21:4(c) MP6: relational-ops
import math
# Given record type, represented by an object with public fields.
class Result:
    def __init__(self):
        self.Done = False
        self.Value = 0.0

# Provided analogue of the insert's numeric predicate.
def IS_NUM(Text):
    try:
        return math.isfinite(float(Text))
    except ValueError:
        return False

def Evaluate(NumStr1,NumStr2):
    RetVal=Result()
    RetVal.Done=False
    if IS_NUM(NumStr1) and IS_NUM(NumStr2):
        Num1=float(NumStr1)
        Num2=float(NumStr2)
        if True:
            RetVal.Value=Num1/Num2
            RetVal.Done=True
    return RetVal
