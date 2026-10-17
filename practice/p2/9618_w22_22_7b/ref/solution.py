# Provided global parallel arrays, QP [1:500]; Python index = QP index - 1.
ErrCode=[999]*500
ErrText=['']*500

def SortArrays():
    Boundary=499
    NoSwaps=False
    while not NoSwaps:
        NoSwaps=True
        for J in range(Boundary):
            if ErrCode[J]==999:
                break
            if ErrCode[J]>ErrCode[J+1]:
                ErrCode[J],ErrCode[J+1]=ErrCode[J+1],ErrCode[J]
                ErrText[J],ErrText[J+1]=ErrText[J+1],ErrText[J]
                NoSwaps=False
        Boundary-=1
