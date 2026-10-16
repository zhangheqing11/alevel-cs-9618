MAX_SIZE = 8
stack = [""] * MAX_SIZE   # ARRAY of 8 STRING -> indexes 0 to 7
top_pointer = -1          # -1 means the stack is empty


def push(item: str) -> bool:
    """Return False if the stack is full; otherwise add item at the top and return True."""
    raise NotImplementedError


def pop() -> str:
    """Return "" if the stack is empty; otherwise remove and return the top item."""
    raise NotImplementedError
