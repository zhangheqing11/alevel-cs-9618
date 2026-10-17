def Status(Actual,Min,Max):
    Result='C'
    if Actual>Max+2 or Actual<Min-2:
        Result='R'
    if Actual<Max-2 and Actual>Min+2:
        Result='A'
    return Result
