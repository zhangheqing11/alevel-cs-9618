def Conceal(CardNumber):
    MaskedString=CardNumber[-4:]
    for Count in range(len(CardNumber)-4):
        MaskedString='*'+MaskedString
    return MaskedString
