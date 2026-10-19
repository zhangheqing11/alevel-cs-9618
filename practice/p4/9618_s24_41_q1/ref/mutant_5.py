# MUTANT 9618_s24_41:1(e)(i) MP6 (return-value): no RETURN -1 after the loop (returns None when not found).
# Question1_J24 -- reference solution (close to the MS Python example)

# ---- 1(a) ----
DataStored = [0] * 20  # global array, 20 elements of type INTEGER
NumberItems = 0  # global INTEGER: quantity of items in DataStored


# ---- 1(b) ----
def Initialise():
    global NumberItems
    Quantity = int(input("How many numbers will you enter (1 to 20)? "))
    while Quantity < 1 or Quantity > 20:
        Quantity = int(input("How many numbers will you enter (1 to 20)? "))
    for Count in range(0, Quantity):
        DataStored[NumberItems] = int(input("Enter number: "))
        NumberItems = NumberItems + 1


# ---- 1(d)(i) ----
def BubbleSort():
    for Count in range(0, NumberItems - 1):
        for Count2 in range(0, NumberItems - 1 - Count):
            if DataStored[Count2] > DataStored[Count2 + 1]:
                Temp = DataStored[Count2]
                DataStored[Count2] = DataStored[Count2 + 1]
                DataStored[Count2 + 1] = Temp


# ---- 1(e)(i) ----
def BinarySearch(DataToFind):
    First = 0
    Last = NumberItems - 1
    while First <= Last:
        MidValue = (First + Last) // 2
        if DataToFind == DataStored[MidValue]:
            return MidValue
        if DataToFind < DataStored[MidValue]:
            Last = MidValue - 1
        else:
            First = MidValue + 1


def OutputData():
    for X in range(0, NumberItems):
        print(DataStored[X], end=" ")
    print()


# ---- main program ----
if __name__ == "__main__":
    # 1(c)(i)
    NumberItems = 0
    Initialise()
    OutputData()
    # 1(d)(ii)
    BubbleSort()
    OutputData()
    # 1(e)(ii)
    Search = int(input("Enter a number to find: "))
    print(BinarySearch(Search))
