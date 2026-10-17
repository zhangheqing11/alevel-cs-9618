# Provided global grade boundaries, QP [1:5], Python index = QP - 1.
GradeBoundary=[65,57,43,35,27]

def CheckMark(Mark):
    for Index in range(5):
        Lower=GradeBoundary[Index]-2
        Upper=GradeBoundary[Index]+2
        if Mark>=Lower and Mark<=Upper:
            return True
    return False

# QP does not specify capacity; provide enough rows for the sample.
Result=[[0,0] for _ in range(100)]

def CheckAll(CNum):
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
