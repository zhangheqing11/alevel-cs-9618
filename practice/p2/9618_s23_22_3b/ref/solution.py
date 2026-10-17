FileName = "queue.txt"  # Python interface name; not specified by the QP.

# Provided ADT adapter; the increased capacity is illustrative, not a QP limit.
Queue = [""] * 20  # 20 STRING locations; Python indices 0..19.
FrontPointer = 0
RearPointer = 0


def AddToQueue(Value):
    global RearPointer
    if RearPointer == len(Queue):
        return False
    Queue[RearPointer] = Value
    RearPointer += 1
    return True


def FileToQueue():
    Added = True
    with open(FileName, encoding="utf-8") as Source:
        Line = Source.readline()
        while Line != "" and Added:
            Added = AddToQueue(Line.rstrip("\n"))
            if Added:
                Line = Source.readline()
