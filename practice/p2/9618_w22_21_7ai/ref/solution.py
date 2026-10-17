def Calculate(Expression):
    for Index in range(len(Expression)):
        ThisChar=Expression[Index]
        if ThisChar<'0' or ThisChar>'9':
            Par1=Expression[:Index]
            Par2=ThisChar
            Par3=Expression[Index+1:]
    Val1=int(Par1)
    Val2=int(Par3)
    if Par2=='+':
        Result=Val1+Val2
    elif Par2=='-' or Par2=='−':
        Result=Val1-Val2
    elif Par2=='*':
        Result=Val1*Val2
    else:
        Result=Val1/Val2
    print(Result)
