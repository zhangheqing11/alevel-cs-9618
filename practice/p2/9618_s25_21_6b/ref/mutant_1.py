# 9618_s25_21:6(b) MP7: array-2d
# Provided INTEGER ARRAY[1:2000,1:2]; zero-based Python rows/columns.
Reading=[[0,0] for _ in range(2000)]

def Sort():
    Boundary=1999
    NoSwaps=False
    while not NoSwaps:
        NoSwaps=True
        for J in range(Boundary):
            if Reading[J][0]>Reading[J+1][0]:
                Reading[J][0],Reading[J+1][0]=Reading[J+1][0],Reading[J][0]
                NoSwaps=False
        Boundary-=1
