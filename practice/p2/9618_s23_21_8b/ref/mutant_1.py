# 9618_s23_21:8(b) MP2: field-extract
def CheckNewItem(NewLine):
    NewItemNum=NewLine[:3]
    with open('Stock.txt',encoding='utf-8') as Handle:
        for ThisLine in Handle:
            ThisItemNum=ThisLine[:4]
            if ThisItemNum==NewItemNum:
                return False
            if ThisItemNum>NewItemNum:
                return True
    return True
