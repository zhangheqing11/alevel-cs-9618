class Node:
    def __init__(self, Data="", Pointer=0):
        self.Data = Data
        self.Pointer = Pointer


# Provided ARRAY[1:200] OF Node, plus an unused slot 0.
# Python indices equal QP pointers; 0 remains the null pointer.
List = [Node() for _ in range(201)]
HeadPointer = 0


def main():
    """Implement the algorithm described in task.md."""
    raise NotImplementedError
