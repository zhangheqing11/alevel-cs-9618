# 9618_s23_21:8(b) MP7: return-value
def CheckNewItem(NewLine):
    NewItemNum=NewLine[:4]
    with open('Stock.txt',encoding='utf-8') as Handle:
        for ThisLine in Handle:
            ThisItemNum=ThisLine[:4]
            if ThisItemNum==NewItemNum:
                return True
            if ThisItemNum>NewItemNum:
                return True
    return True
