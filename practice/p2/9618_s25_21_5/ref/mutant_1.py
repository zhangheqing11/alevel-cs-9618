# 9618_s25_21:5 MP7: queue-array.
# Test adapter: QP does not prescribe array names, capacity or index origin.
# 100 STRING locations each; Python indices 0..99.
Stack = [""] * 100
Queue = [""] * 100
TopOfStack = -1  # Index of last item; -1 means empty.
FrontPointer = 0  # Next item to remove.
RearPointer = 0  # Next location to add; equal pointers mean empty.


def main():
    global TopOfStack, FrontPointer, RearPointer
    while TopOfStack >= 0:
        Item = Stack[TopOfStack]
        TopOfStack -= 1
        Queue[RearPointer] = Item
        RearPointer += 1
    while FrontPointer < RearPointer:
        Item = Queue[FrontPointer]
        FrontPointer = RearPointer
        TopOfStack += 1
        Stack[TopOfStack] = Item
