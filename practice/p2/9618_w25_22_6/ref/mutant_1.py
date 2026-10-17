# 9618_w25_22:6 MP5: char-compare
def Compare(String1,String2,CaseMatters,Position):
    S1Length=len(String1)
    if len(String2)<S1Length:
        return False
    if CaseMatters:
        String1=String1.upper()
        String2=String2.upper()
    if Position=='e':
        String2=String2[len(String2)-S1Length:]
    else:
        String2=String2[:S1Length]
    return String1==String2
