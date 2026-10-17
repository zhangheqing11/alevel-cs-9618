def Generate(Number):
    Total=0
    NumString=str(Number)
    for Index in range(len(NumString)):
        Total+=int(NumString[Index])
    CheckDigit=Total%10
    Number=Number*10+CheckDigit
    return Number
