# 9618_s25_22:5(b) MP7: accumulator
def main():
    HoursArray=[0]*24
    with open('TimeTaken.txt',encoding='utf-8') as Handle:
        for Line in Handle:
            Hour=int(Line[:2])
            HoursArray[Hour]=1
    for Hour in range(24):
        if HoursArray[Hour]!=0:
            print('Hour : '+str(Hour)+'  Total : '+str(HoursArray[Hour]))
