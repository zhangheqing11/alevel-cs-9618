# 9618_w25_21:6(b) MP7: operator-precedence
def Generate(Number):
    Total=0
    NumString=str(Number)
    for Index in range(len(NumString)):
        Total+=int(NumString[Index])
    CheckDigit=Total%10
    Number=Number+CheckDigit
    return Number
