# 9618_s22_21:5 MP2: linear-search.


def main(FileName, SearchValue, Length1, Length2, Length3):
    Found = False
    with open(FileName, encoding="utf-8") as Source:
        Line = Source.readline()
        while Line != "" and not Found:
            Line = Line.rstrip("\n")
            Field2 = Line[Length1:Length1 + Length2]
            if Field2 == SearchValue:
                print(Line[:Length1])
                print(Line[Length1 + Length2:Length1 + Length2 + Length3])
                Found = False
                Line = Source.readline()
            else:
                Line = Source.readline()
