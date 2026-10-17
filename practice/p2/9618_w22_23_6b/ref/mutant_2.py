# 9618_w22_23:6(b) MP4: logic-ops
def Status(Actual,Min,Max):
    Result='C'
    if Actual>Max+2 or Actual<Min-2:
        Result='R'
    if Actual<Max-2 or Actual>Min+2:
        Result='A'
    return Result
