# 9618_s24_23:4(a) MP6: operator-precedence
TotalA = 0.0  # Global REAL
TotalB = 0.0  # Global REAL

def TwoParts():
    global TotalA,TotalB
    TotalA=0.0
    TotalB=0.0
    NextNum=float(input())
    while NextNum!=0:
        TotalA+=NextNum
        NextNum=float(input())
    NextNum=float(input())
    while NextNum!=0:
        TotalB+=NextNum
        NextNum=float(input())
    print('The average is',TotalA+TotalB/2)
