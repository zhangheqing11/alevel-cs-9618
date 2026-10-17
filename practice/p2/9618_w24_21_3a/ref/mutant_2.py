# 9618_w24_21:3(a) MP4: file-close.


def main():
    LineX = LineY = LineZ = ""
    if True:
        Source = open("Result.txt", encoding="utf-8")
        Line = Source.readline()
        while Line != "":
            ThisLine = Line.rstrip("\n")
            LineX = LineY
            LineY = LineZ
            LineZ = ThisLine
            Line = Source.readline()
    print(LineX)
    print(LineY)
    print(LineZ)
