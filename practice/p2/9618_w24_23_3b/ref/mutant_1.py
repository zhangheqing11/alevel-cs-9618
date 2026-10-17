# 9618_w24_23:3(b) MP3: linked-list
# Provided QP record and array. Keep QP indices and pointer values with a dummy slot 0.
class Node:
    def __init__(self,Data='',Pointer=0):
        self.Data=Data
        self.Pointer=Pointer
List=[None]+[Node() for _ in range(200)]
HeadPointer=0

def main():
    for Index in range(1,200):
        List[Index].Pointer=Index
    List[200].Pointer=0
