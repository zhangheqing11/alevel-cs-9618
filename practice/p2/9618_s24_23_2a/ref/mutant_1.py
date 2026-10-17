# 9618_s24_23:2(a) MP5: array-index.
# Provided global 1D array of STRING; QP gives no name or capacity.
# This example has 64 elements, more than the sample file lines.
# Python index = chosen pseudocode index (starting at 1) - 1.
Data = [""] * 64
FileName = "data.txt"


def main():
    Index = 0
    with open(FileName, encoding="utf-8") as Source:
        Line = Source.readline()
        while Line != "":
            Data[0] = Line.rstrip("\n")
            Index += 1
            Line = Source.readline()
