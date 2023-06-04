import time
import math
import os

# A simple stardate converter
# using the algorithm given by David Trimboli(david@trimboli.name) at http://www.trimboli.name/stardate.html
# the script can convert between the normal Earth calendar and the stardate from Star Trek
# finished at stardate 23424.1

def cal_to_stardate(localtime):
    #convert normal Earth calendar to stardate
    #tm_century = tm_year // 100 + 1
    tm_cyear = localtime.tm_year % 100
    if tm_cyear%4 == 1:
        tm_cday = 366 + tm_cyear // 4 * 1461 + localtime.tm_yday - 1
    elif tm_cyear%4 == 2:
        tm_cday = 366 + tm_cyear // 4 * 1461 + 365 + localtime.tm_yday - 1
    elif tm_cyear%4 == 3:
        tm_cday = 366 + tm_cyear // 4 * 1461 + 365*2 + localtime.tm_yday - 1
    else:
        tm_cday = 366 + tm_cyear // 4 * 1461 - 365 + localtime.tm_yday - 1

    tm_cday += (localtime.tm_hour * 60 + localtime.tm_min) / (24*60)
    #print(tm_cday)
    stardate = tm_cday / 36525 * 100000
    stardate = round(stardate, 3) 
    #change the accuracy by 1-3;   default using 3 decimals with the accuracy of minutes
    print("Stardate:", stardate)

def stardate_to_cal(stardate):
    #convert stardate to Earth calendar
    tm_cday = stardate / 100000 *36525
    tm_clock = round(tm_cday % 1 * (24*60))
    tm_hour = tm_clock // 60
    tm_min = tm_clock % 60
    tm_cday = math.floor(tm_cday)
    sum, days = 0, 366
    while True:
        if days >= tm_cday:
            if sum % 4 == 0:
                days -= 1
            days -= 365
            sum -= 1
            break
        sum += 1
        days += 365
        if sum % 4 == 0:
            days += 1
        #print(days,sum)        
    tm_year = sum + 1
    tm_yday = tm_cday - days + 1
    cal_date_str = "20" + str(tm_year) + "-" + str(tm_yday) + "-" + str(tm_hour) + "-" + str(tm_min) 
    #the algorithm is capable of calculating in the 21C
    cal_date_tuple = time.strptime(cal_date_str, "%Y-%j-%H-%M")
    calendar_date = time.strftime("%Y-%m-%d-%H-%M", cal_date_tuple)
    print(calendar_date)


os.system("cls")
mode = input('''Get current stardate [1]
Get former stardate[2]
Get Earth calendar from stardate[3]
''')

if mode == "1":
    os.system("cls")
    localtime = time.localtime(time.time())
    cal_to_stardate(localtime)
    #print(localtime)  
elif mode == "2":
    os.system("cls")
    raw_former_time = input("What time?[YYYY-MM-DD-hh-mm]")
    former_time = time.strptime(raw_former_time,"%Y-%m-%d-%H-%M")
    cal_to_stardate(former_time)
elif mode == "3":
    os.system("cls")
    stardate = float(input("Input stardate:"))
    stardate_to_cal(stardate)
else:
    os.system("cls")
    print("Unidentified input, returning default current stardate")
    localtime = time.localtime(time.time())
    cal_to_stardate(localtime)


