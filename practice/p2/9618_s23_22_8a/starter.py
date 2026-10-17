# Provided module from the QP; alphabetic means the ASCII letter ranges.
def OnlyAlpha(Text):
    for c in Text:
        if not ('A'<=c<='Z' or 'a'<=c<='z'):
            return False
    return True

def CheckInfo(NewLine):
    """Implement the QP algorithm; preserve this public interface."""
    raise NotImplementedError
