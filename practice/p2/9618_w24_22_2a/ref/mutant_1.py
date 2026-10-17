# 9618_w24_22:2(a) MP5: loop-bounds
def Conceal(CardNumber):
    MaskedString=CardNumber[-4:]
    for Count in range(len(CardNumber)-3):
        MaskedString='*'+MaskedString
    return MaskedString
