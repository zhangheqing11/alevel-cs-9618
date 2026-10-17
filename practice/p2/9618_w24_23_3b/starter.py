# Provided QP record and array. Keep QP indices and pointer values with a dummy slot 0.
class Node:
    def __init__(self,Data='',Pointer=0):
        self.Data=Data
        self.Pointer=Pointer
List=[None]+[Node() for _ in range(200)]
HeadPointer=0

def main():
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
