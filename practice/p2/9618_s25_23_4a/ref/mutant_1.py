# 9618_s25_23:4(a) MP4: relational-ops.


def main():
    Week = 1
    with open("Sales.txt", encoding="utf-8") as Source:
        Line = Source.readline()
        while Line != "":
            Sales = int(Line)
            if Sales >= 500:
                print(Week)
            Week += 1
            Line = Source.readline()
