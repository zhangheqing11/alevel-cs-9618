def Parity(BitString):
    Count=0
    for Bit in BitString:
        if Bit=='1':
            Count+=1
    if Count%2==1:
        BitString+='1'
    else:
        BitString+='0'
    return BitString
