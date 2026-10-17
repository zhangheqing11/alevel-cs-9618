# Provided INTEGER ARRAY[1:6,1:3], QP example; Python row/column = QP - 1.
# Unused row's last two values are arbitrary integers, not meaningful defaults.
RouteTable=[[100,199,1],[200,259,2],[-1,0,0],[260,399,2],[400,599,3],[600,999,1]]

def GetPort(ThisDest):
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
