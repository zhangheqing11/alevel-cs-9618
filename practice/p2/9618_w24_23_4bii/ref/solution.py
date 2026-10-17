# GB [1:5]: Python index = QP - 1; Check [0:75]: no conversion.
GB=[65,57,43,35,27]
Check=[False]*76

def GBInitialise():
    for ThisIndex in range(76):
        Check[ThisIndex]=False
    for GBIndex in range(5):
        GBMark=GB[GBIndex]
        for ThisIndex in range(GBMark-2,GBMark+3):
            Check[ThisIndex]=True
