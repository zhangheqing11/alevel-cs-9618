# Provided INTEGER ARRAY[1:100]; Python index = QP index - 1.
Data=[0]*100

def Check():
    Odd=0
    Even=0
    for Index in range(100):
        if (Index+1)%2==0:
            Even+=Data[Index]
        else:
            Odd+=Data[Index]
    if Odd>Even:
        return 'Odd'
    if Even>Odd:
        return 'Even'
    return 'Same'
