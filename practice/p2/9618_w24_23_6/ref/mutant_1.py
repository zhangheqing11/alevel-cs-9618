# 9618_w24_23:6 MP3: loop-bounds
from datetime import date

def AdjustClock(ThisYear):
    ThisDayNumber=0
    SundayCount=0
    while SundayCount!=2:
        ThisDayNumber+=1
        ThisDate=date(ThisYear,3,ThisDayNumber)
        if ThisDate.weekday()==6:
            SundayCount+=1
    return ThisDayNumber
