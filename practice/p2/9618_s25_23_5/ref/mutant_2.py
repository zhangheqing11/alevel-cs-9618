# 9618_s25_23:5 MP4: char-compare
def Parity(BitString):
    Count=0
    for Bit in BitString:
        if Bit=='0':
            Count+=1
    if Count%2==1:
        BitString+='1'
    else:
        BitString+='0'
    return BitString
