# 9618_w23_22:4(a) MP5: div-mod
def Count():
    COdd=0
    CEven=0
    ThisNum=int(input())
    while ThisNum!=99:
        if ThisNum%2==0:
            COdd+=1
        else:
            CEven+=1
        ThisNum=int(input())
    print('Count of odd and even numbers:',COdd,CEven)
