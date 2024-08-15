import datetime
print(dir(datetime))
# Output:
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

from datetime import datetime
now = datetime.now()
print(now)                      # Output: 2024-08-16 08:26:49.219717
day = now.day                   # Output: 16
month = now.month               # Output: 8
year = now.year                 # Output: 2024
hour = now.hour                 # Output: 8
minute = now.minute             # Output: 26
second = now.second             # Output: 49
timestamp = now.timestamp()     # Output: 1692268009.219717
print(day, month, year, hour, minute)
# Output: 16 8 2024 8 26
print('timestamp', timestamp)
# Output: timestamp 1692268009.219717
print(f'{day}/{month}/{year}, {hour}:{minute}')  # Output: 16/8/2024, 8:26

from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # Output: 2020-01-01 00:00:00
day = new_year.day   # Output: 1
month = new_year.month # Output: 1
year = new_year.year # Output: 2020
hour = new_year.hour # Output: 0
minute = new_year.minute # Output: 0
second = new_year.second # Output: 0
print(day, month, year, hour, minute) # Output: 1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # Output: 1/1/2020, 0:0

from datetime import datetime
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
# Output: time: 08:26:49
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)
# Output: time one: 08/16/2024, 08:26:49
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two:", time_two)
# Output: time two: 16/08/2024, 08:26:49

from datetime import datetime
date_string = "20 October, 2024"
print("date_string =", date_string)
# Output: date_string = 20 October, 2024
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
# Output: date_object = 2024-10-20 00:00:00

from datetime import date
d = date(2020, 1, 1)
print(d)
# Output: 2020-01-01
print('Current date:', d.today())    
# Output: Current date: 2024-08-16
today = date.today()
print("Current year:", today.year)   # Output: Current year: 2024
print("Current month:", today.month) # Output: Current month: 8
print("Current day:", today.day)     # Output: Current day: 16

from datetime import time
a = time()
print("a =", a)
# Output: a = 00:00:00
b = time(10, 30, 50)
print("b =", b)
# Output: b = 10:30:50
c = time(hour=10, minute=30, second=50)
print("c =", c)
# Output: c = 10:30:50
d = time(10, 30, 50, 200555)
print("d =", d)
# Output: d = 10:30:50.200555

today = date(year=2024, month=8, day=16)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)
# Output: Time left for new year:  138 days, 0:00:00

t1 = datetime(year = 2024, month = 8, day = 16, hour = 8, minute = 26, second = 49) 
t2 = datetime(year = 2025, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)
# Output: Time left for new year: 138 days, 15:33:11

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
# Output: t3 = 86 days, 22:56:50


print('''
 #Created by: Ayesha Noreen |Follow us on www.linkedin.com/in/khatoonintech | We love #AUGUSTHON 💕
      ''')