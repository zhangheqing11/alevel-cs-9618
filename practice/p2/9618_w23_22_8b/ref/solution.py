MyID = '123'  # Global STRING, changed by the caller.
# INTEGER array [1:6,1:3]; Python indices = pseudocode indices - 1.
RouteTable = [[100,199,1],[200,259,2],[-1,0,0],[260,399,2],[400,599,3],[600,999,1]]
MessageStacks = [[],[]]  # Provided stack service; capacity is outside this question.
def StackMsg(ThisMsg,StackNum):
    MessageStacks[StackNum-1].append(ThisMsg)
    return True

def ProcessMsg(ThisMsg):
    if len(ThisMsg)>=4:
        ThisDest=ThisMsg[:3]
        if ThisDest==MyID:
            StackNum=1
        else:
            StackNum=2
        Response=StackMsg(ThisMsg,StackNum)
        if not Response:
            print('Message discarded - no room on stack')
