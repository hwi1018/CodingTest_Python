from datetime import datetime

def GetYear1000Days(start_year):
    day = 0  
    for y in range(start_year, start_year+1000):
        if(y % 400==0):
            day += 366
        elif(y % 100 ==0):
            day += 365
        elif(y % 4 ==0):
            day +=366
        else:
            day +=365
    return day

today = list(map(int, input().split()))
dday = list(map(int, input().split()))

today_date = datetime(today[0], today[1], today[2])
dday_date = datetime(dday[0], dday[1], dday[2])

# 날짜 구하는 방법
ddays = (dday_date - today_date).days

year1000Days = GetYear1000Days(today[0])

if (year1000Days <= ddays):
    print('gg')
else:
    print("D-{0}".format(ddays))
