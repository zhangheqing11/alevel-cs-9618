# 9618_s24_23:2(a) MP1: file-close.
# Provided global 1D array of STRING; QP gives no name or capacity.
# This example has 64 elements, more than the sample file lines.
# Python index = chosen pseudocode index (starting at 1) - 1.
Data = [""] * 64
FileName = "data.txt"


def main():
    Index = 0
    if True:
        Source = open(FileName, encoding="utf-8")
        Line = Source.readline()
        while Line != "":
            Data[Index] = Line.rstrip("\n")
            Index += 1
            Line = Source.readline()
