# 9618_s25_21:7(a) MP4: accumulator
def CustomerOrder(Number,Points):
    NewPoints=Points+Number
    NumberFree=0
    while NewPoints>=11 and Number>0:
        NumberFree+=1
        NewPoints-=10
        Number-=1
    print('Number of free coffees is:',NumberFree)
    return NewPoints
