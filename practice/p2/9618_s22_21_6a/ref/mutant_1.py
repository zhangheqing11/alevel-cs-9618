# 9618_s22_21:6(a) MP3: div-mod
def main():
    Count = 0
    for ThisInt in range(100, 201):
        if ThisInt % 10 == 6:
            print(ThisInt)
            Count += 1
    print(Count)
