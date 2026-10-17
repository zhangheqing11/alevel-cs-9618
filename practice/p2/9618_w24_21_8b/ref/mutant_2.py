# 9618_w24_21:8(b) MP7: array-2d
# Provided global grade boundaries, QP [1:5], Python index = QP - 1.
GradeBoundary=[65,57,43,35,27]

def CheckMark(Mark):
    for Index in range(5):
        Lower=GradeBoundary[Index]-2
        Upper=GradeBoundary[Index]+2
        if Mark>=Lower and Mark<=Upper:
            return True
    return False

# QP does not specify capacity; provide enough rows for the sample.
Result=[[0,0] for _ in range(100)]

def CheckAll(CNum):
    Count=0
    with open('GRList.txt','w',encoding='utf-8') as Handle:
        for Index in range(CNum):
            if CheckMark(Result[Index][0]):
                Handle.write(str(Result[Index][0])+'\n')
                Count+=1
    print('There are '+str(Count)+' papers to check')
