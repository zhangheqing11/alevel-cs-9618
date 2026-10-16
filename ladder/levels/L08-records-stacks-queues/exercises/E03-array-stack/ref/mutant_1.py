# M1: intentional fault from spec.md.
MAX_SIZE = 8
stack = [""] * MAX_SIZE   # ARRAY of 8 STRING -> indexes 0 to 7
top_pointer = -1          # -1 means the stack is empty


def push(item: str) -> bool:
    if top_pointer == MAX_SIZE - 1:
        return False
    top_pointer = top_pointer + 1
    stack[top_pointer] = item
    return True


def pop() -> str:
    if top_pointer == -1:
        return ""
    item = stack[top_pointer]
    top_pointer = top_pointer - 1
    return item
