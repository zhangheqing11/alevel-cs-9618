HH = 0  # Global INTEGER
MM = 0  # Global INTEGER
SS = 0  # Global INTEGER
# Provided callbacks, observed separately by tests.
def CheckAlarm():
    pass

def NewDay():
    pass

def Tick():
    raise NotImplementedError
