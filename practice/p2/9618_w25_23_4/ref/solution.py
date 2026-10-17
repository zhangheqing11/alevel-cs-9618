# Provided INTEGER ARRAY[1:20] and sample global STRING; Python index = QP - 1.
Data=[0]*20
NumString='101,456,219,754,328'

def Store():
    Index=0
    StartPos=0
    while StartPos<len(NumString) and Index<20:
        ThisString=NumString[StartPos:StartPos+3]
        Data[Index]=int(ThisString)
        Index+=1
        StartPos+=4
