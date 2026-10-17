# Provided stack state, QP p6. ARRAY[500:506] OF STRING.
# Python index = QP memory location - 500.
Stack = ["PPP", "NNN", "ZZZ", "XXX", "YYY", "WWW", ""]
BottomOfStack = 500
TopOfStack = 505
FileName = "Stack.txt"  # Python test filename; QP does not name it.


def POP():
    global TopOfStack
    if TopOfStack < BottomOfStack:
        raise IndexError("Empty stack")
    Value = Stack[TopOfStack - 500]
    TopOfStack -= 1
    return Value


def SaveStack():
    """Implement the algorithm described in task.md."""
    raise NotImplementedError
