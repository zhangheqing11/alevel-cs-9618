# 9618_s24_22:6(a) MP4: loop-bounds
def Trim(Name):
    if len(Name)<=16:
        return Name
    while len(Name)>14:
        while Name[-1]!=' ':
            Name=Name[:-1]
        Name=Name[:-1]
    return Name+'...'
