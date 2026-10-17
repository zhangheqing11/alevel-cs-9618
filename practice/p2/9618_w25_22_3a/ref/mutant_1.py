# 9618_w25_22:3(a) MP4: string-concat.


def main():
    with open("OldFile.txt", encoding="utf-8") as Source:
        with open("NewFile.txt", "w", encoding="utf-8") as Target:
            LineX = Source.readline()
            while LineX != "":
                LineX = LineX.rstrip("\n")
                LineY = Source.readline().rstrip("\n")
                LineZ = Source.readline().rstrip("\n")
                NewString = LineX + LineY + LineZ
                Target.write(NewString + "\n")
                LineX = Source.readline()
