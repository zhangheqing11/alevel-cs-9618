# 9618_w24_21:3(a) MP2: loop-to-eof.


def main():
    LineX = LineY = LineZ = ""
    with open("Result.txt", encoding="utf-8") as Source:
        Line = Source.readline()
        for Count in range(3):
            ThisLine = Line.rstrip("\n")
            LineX = LineY
            LineY = LineZ
            LineZ = ThisLine
            Line = Source.readline()
    print(LineX)
    print(LineY)
    print(LineZ)
