# 9618_w23_21:4(a) MP4: loop-bounds
# Provided STRING ARRAY[1:150]; Python index = QP index - 1.
Data=['']*150

def TooMany(Search,Max):
    Count=0
    for Index in range(149):
        if Data[Index]==Search:
            Count+=1
    return Count>Max
