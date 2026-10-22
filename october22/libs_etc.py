# built-in library
# import, from import, from import as. math, random, json, os, sys
# math (sqrt, pi),
import math

print(math.pi)
print(math.sqrt(18))

# random (random(), randint(1,6), randrange(0,10,2), uniform(1.5,3.5)
# choice(["a","b","c"]), choices(sequence, k=5), sample(range(1,50), 6), shuffle(lst)
# )
import random

print("random.random()")
print(random.random())
print(100 + int(random.random() * 100))
print("random.randint()")
print(random.randint(100, 200))
print(random.randrange(20, 40, 3))
print(random.uniform(1.5, 3.5))
print(random.choice(["a", "b", "C", "D"]))
print(random.choices(["a", "b", "C", "D"], k=2))
lst = ["a", "b", "c", "d", "e", "f", "g"]
print(lst)
random.shuffle(lst)
print(lst)

import json
obj = ["BB", "CC", "DD"]
print(type(obj))
st = json.dumps(obj)
print(type(st))
input_st = '["a", "b", "c", "d", "e", "f", "g"]'
print(type(input_st))
mylist = json.loads(input_st)
print(type(mylist))
print(mylist)

bigstr = """
{
  "name": "Иван",
  "age": 30,
  "isStudent": false,
  "skills": ["JavaScript", "Python", "JSON"]
}
"""
mydict = json.loads(bigstr)
print(type(mydict))
print(mydict)


# f = open('file.txt', 'r')
# json (dumps(obj), loads(s), dump(obj, f), load(f))
# dumps(ensure_ascii=False, indent=2, sort_keys=True)
# types mapping in json

# import datetime
# current_datetime = datetime.datetime.now()
# print(current_datetime)

from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.date())
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.second)
print(datetime.today())

import zoneinfo

from datetime import timedelta
tz = zoneinfo.ZoneInfo("America/New_York")
now_in_NYC = datetime.now(tz)
print(now_in_NYC)

date1 = datetime(2026, 10, 22)
date2 = datetime(2026, 8, 1)
dates_diff = date1 - date2
print(type(dates_diff))
print(date1 + timedelta(days=60))
print(date1 - timedelta(days=60))
print(current_datetime - timedelta(minutes=301))
datetime1 = datetime.now()
datetime2 = datetime1 - timedelta(days=7, hours=3, minutes=40)
print("datetime1", datetime1)
print("datetime2", datetime2)
mydiff = datetime2 - datetime1
print(mydiff)
print(mydiff.days)
print(mydiff.total_seconds())
# datetime (now(), year, month, day, hour, minute, second, today(), timedelta(days=7),
# -timedelta(days=7))
# diff = date(2026, 10, 20) - date(2026, 10, 1)
from datetime import date
if date(2026, 10, 20) < date(2026, 10, 1):
    print("less than")
# diff.days
# diff.total_seconds()
# now = datetime.now(<class 'dict'>)
now = datetime.now()
print(now)
print(now.strftime("%d.%m.%Y"))
print(now.strftime("%Y_-a%m5-.%d"))
print(now.strftime("%H:%M:%S"))
d = None
try:
    d = datetime.strptime("16..10.2026", "%d.%m.%Y")
except ValueError:
    pass
print(d)
#
# weekday(): Понедельник = 0
print(now.weekday())
print(now.month)
# pip(install, freeze), uv, poetry
# requests

import requests

response = requests.get('https://mig.kz')

if response.status_code == 200:
    # data = response.json()
    a = 0
else:
    print("Ошибка при выполнении запроса")

