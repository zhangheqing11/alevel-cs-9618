

def main():
    LineX = LineY = LineZ = ""
    with open("Result.txt", encoding="utf-8") as Source:
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
