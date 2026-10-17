# 9618_w24_21:8(a) MP4: relational-ops
# Provided global grade boundaries, QP [1:5], Python index = QP - 1.
GradeBoundary=[65,57,43,35,27]

def CheckMark(Mark):
    for Index in range(5):
        Lower=GradeBoundary[Index]-2
        Upper=GradeBoundary[Index]+2
        if Mark>Lower and Mark<=Upper:
            return True
    return False
