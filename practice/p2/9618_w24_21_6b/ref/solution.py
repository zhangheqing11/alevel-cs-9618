from datetime import date
# Provided [1:12]; Python index = month - 1. Leap years excluded by QP.
DaysInMonth=[31,28,31,30,31,30,31,31,30,31,30,31]

def GetDate(ProductionDate,ShelfLife):
    DD=ProductionDate.day+ShelfLife
    MM=ProductionDate.month
    YY=ProductionDate.year
    LastDay=DaysInMonth[MM-1]
    if DD>LastDay:
        DD-=LastDay
        MM+=1
        if MM==13:
            MM=1
            YY+=1
    return date(YY,MM,DD)
