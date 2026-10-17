# 9618_w24_21:2 MP7: boundary-values
HH = 0  # Global INTEGER
MM = 0  # Global INTEGER
SS = 0  # Global INTEGER
# Provided callbacks, observed separately by tests.
def CheckAlarm():
    pass

def NewDay():
    pass

def Tick():
    global HH,MM,SS
    SS+=1
    if SS==60:
        SS=0
        MM+=1
        if MM==60:
            MM=0
            HH+=1
            if HH==23:
                HH=0
                NewDay()
        CheckAlarm()
