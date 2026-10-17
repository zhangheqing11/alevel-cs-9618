# 9618_w23_22:4(a) MP6: initialise-variables
def Count():
    COdd=1
    CEven=0
    ThisNum=int(input())
    while ThisNum!=99:
        if ThisNum%2==1:
            COdd+=1
        else:
            CEven+=1
        ThisNum=int(input())
    print('Count of odd and even numbers:',COdd,CEven)
