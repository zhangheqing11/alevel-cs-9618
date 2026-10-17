# 9618_s22_21:6(a) MP5: output-format
def main():
    Count = 0
    for ThisInt in range(100, 201):
        if ThisInt % 10 == 7:
            print(ThisInt)
            Count += 1
    print(Count - 1)
