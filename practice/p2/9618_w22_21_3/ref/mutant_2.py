# 9618_w22_21:3 MP3: loop-bounds.
# Provided ARRAY of 200 INTEGER elements; QP does not state its lower bound.
# With a 1-based pseudocode array, Python index = pseudocode index - 1.
Data = [0] * 200


def main():
    Max = Data[0]
    for Index in range(199):
        if Data[Index] > Max:
            Max = Data[Index]
    print(Max)
