# 9618_w25_23:2(a) MP7: loop-bounds.
# Provided global 1D array of 65 STRING elements (unnamed in the QP).
# With 1-based pseudocode indexing, Python index = pseudocode index - 1.
Data = [""] * 65
FileName = "data.txt"  # Existing file; Python interface name only.


def main():
    with open(FileName, "a", encoding="utf-8") as Target:
        Index = 0
        while Index < 64:
            if Data[Index] != "":
                Target.write(Data[Index] + "\n")
            Index += 1
