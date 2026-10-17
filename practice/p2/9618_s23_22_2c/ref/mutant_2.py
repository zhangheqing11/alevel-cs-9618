# 9618_s23_22:2(c) MP3: array-index.
from datetime import date

MyDOB = date(2023, 6, 22)  # Provided DATE; tests replace it.

# Provided insert function: Sunday = 1, ..., Saturday = 7.
def DAYINDEX(Value):
    return (Value.weekday() + 1) % 7 + 1


def main():
    global Days
    # ARRAY[1:7] OF STRING; Python index = pseudocode index - 1.
    Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    Index = DAYINDEX(MyDOB)
    print(Days[Index - 1])
