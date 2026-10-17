# 9618_s25_23:7(b)(ii) MP4: date-functions
from datetime import date
LastVisitDateString = ''  # Given STRING, set by the caller.
DayInt = 0  # INTEGER
MonthInt = 0  # INTEGER
YearInt = 0  # INTEGER
LastVisitDate = date(2000,1,1)  # DATE

def main():
    global DayInt,MonthInt,YearInt,LastVisitDate
    DayInt=int(LastVisitDateString[:2])
    MonthInt=int(LastVisitDateString[2:4])
    YearInt=int(LastVisitDateString[-4:])
    LastVisitDate=LastVisitDateString
