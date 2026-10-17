# Provided receiver: tests inject a finite sequence, never wait on a real network.
def GetData():
    return '****'

def ReceiveFile(FileName):
    """Implement the QP algorithm; preserve the public interface."""
    raise NotImplementedError
