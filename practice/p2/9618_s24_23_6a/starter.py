# Provided display interface: this Python adapter records the filename by printing it.
def Display(Filename):
    print(Filename)

def Progress(Percent,Root):
    """Implement the QP algorithm; preserve this public interface."""
    raise NotImplementedError
