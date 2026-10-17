# 9618_s25_22:5(b) MP7: accumulator
def main():
    with open('TimeTaken.txt',encoding='utf-8') as Handle:
        Line=Handle.readline()
        Hour=Line[:2]
        Count=1
        for Line in Handle:
            NextHour=Line[:2]
            if NextHour==Hour:
                Count=1
            else:
                print('Hour : '+Hour+'  Total : '+str(Count))
                Hour=NextHour
                Count=1
        print('Hour : '+Hour+'  Total : '+str(Count))
