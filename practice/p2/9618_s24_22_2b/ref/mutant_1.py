# 9618_s24_22:2(b) MP4: loop-bounds.
# Provided external modules; tests replace their behaviour.
def GetStat():
    return True


def Reset(Port):
    pass


def main():
    Flag = GetStat()
    while Flag != True:
        for Port in range(1, 3):
            Reset(Port)
        Flag = GetStat()
