# 9618_w22_23:7(a) MP5: relational-ops
# Provided global parallel arrays, QP [1:500]; Python index = QP index - 1.
ErrCode=[999]*500
ErrText=['']*500

def OutputRange():
    First=int(input('First error number: '))
    Last=int(input('Last error number: '))
    print('List of error numbers from '+str(First)+' to '+str(Last))
    Count=0
    for Index in range(500):
        ThisErr=ErrCode[Index]
        if ThisErr>Last:
            break
        if ThisErr>First:
            ThisMess=ErrText[Index]
            if ThisMess=='':
                ThisMess='Error Text Missing'
            print(str(ThisErr)+' : '+ThisMess)
            Count+=1
    print(str(Count)+' error numbers output')
