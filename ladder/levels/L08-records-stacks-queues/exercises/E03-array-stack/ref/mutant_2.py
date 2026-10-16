# M2: intentional fault from spec.md.
MAX_SIZE = 8
stack = [""] * MAX_SIZE   # ARRAY of 8 STRING -> indexes 0 to 7
top_pointer = -1          # -1 means the stack is empty


def push(item: str) -> bool:
    global top_pointer
    if top_pointer == MAX_SIZE:
        return False
    top_pointer = top_pointer + 1
    stack[top_pointer] = item
    return True


def pop() -> str:
    global top_pointer
    if top_pointer == -1:
        return ""
    item = stack[top_pointer]
    top_pointer = top_pointer - 1
    return item
