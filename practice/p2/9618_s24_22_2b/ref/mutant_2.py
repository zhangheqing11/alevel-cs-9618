# 9618_s24_22:2(b) MP1: flowchart-to-pseudocode.
# Provided external modules; tests replace their behaviour.
def GetStat():
    return True


def Reset(Port):
    pass


def main():
    Flag = GetStat()
    while Flag == True:
        for Port in range(1, 4):
            Reset(Port)
        Flag = GetStat()
