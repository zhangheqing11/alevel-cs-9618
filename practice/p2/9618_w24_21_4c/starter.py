import math
# Given record type, represented by an object with public fields.
class Result:
    def __init__(self):
        self.Done = False
        self.Value = 0.0

# Provided analogue of the insert's numeric predicate.
def IS_NUM(Text):
    try:
        return math.isfinite(float(Text))
    except ValueError:
        return False

def Evaluate(NumStr1,NumStr2):
    """Implement the QP algorithm; preserve this public interface."""
    raise NotImplementedError
