# 9618_w22_21:5 MP4: type-conversion
# Provided global INTEGER arrays; Python index = QP index - 1.
Array1=[0]*600
Array2=[0]*200

def Summarise():
    IxB=0
    for IxA in range(0,600,3):
        Value=(Array1[IxA]+Array1[IxA+1]+Array1[IxA+2])/3
        Array2[IxB]=round(Value)
        IxB+=1
