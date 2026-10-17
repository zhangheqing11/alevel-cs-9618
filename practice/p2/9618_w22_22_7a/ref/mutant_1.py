# 9618_w22_22:7(a) MP5: loop-bounds
# Provided global parallel arrays, QP [1:500]; Python index = QP index - 1.
ErrCode=[999]*500
ErrText=['']*500

def OutputError(LineNum,ErrNum):
    for Index in range(499):
        if ErrCode[Index]==ErrNum:
            print(ErrText[Index]+' on line '+str(LineNum))
            return
        if ErrCode[Index]>ErrNum:
            break
    print('Unknown error on line '+str(LineNum))
