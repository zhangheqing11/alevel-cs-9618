# Test adapter: QP does not prescribe array names, capacity or index origin.
# 100 STRING locations each; Python indices 0..99.
Stack = [""] * 100
Queue = [""] * 100
TopOfStack = -1  # Index of last item; -1 means empty.
FrontPointer = 0  # Next item to remove.
RearPointer = 0  # Next location to add; equal pointers mean empty.


def main():
    """Implement the algorithm described in task.md."""
    raise NotImplementedError
