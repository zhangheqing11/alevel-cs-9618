MyID = '202'  # Global STRING, chosen by the caller.
# Provided communication adapters; tests supply deterministic input/output queues.
IncomingData = []
SentMessages = []
def GetData():
    return IncomingData.pop(0)
def Transmit(Message,Port):
    SentMessages.append((Message,Port))

def Chat(Destination,Port):
    """Implement the QP algorithm; preserve this public interface."""
    raise NotImplementedError
