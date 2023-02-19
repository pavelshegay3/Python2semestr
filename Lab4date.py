# 1
import datetime
from datetime import date, timedelta

print("nomer1")
x1 = datetime.datetime.now() - timedelta(5)
print(x1, "\n")
# 2
print("nomer2")
mylist = []
x2 = datetime.date.today() - timedelta(1)
i = 0
while i < 3:
    mylist.append(x2)
    x2 = x2 + timedelta(1)
    i = i + 1
for x in mylist:
    print(x)
print('\n')
print("nomer3")
# 3
x3 = datetime.datetime.now().replace(microsecond=0)
print(x3, '\n')
print("nomer4")
# 4
year = int(input("enter a year: "))
month = int(input("enter a month: "))
day = int(input("enter a day: "))
year1 = int(input("enter another year: "))
month1 = int(input("enter another month: "))
day1 = int(input("enter another day: "))
date = datetime.date(year, month, day)
date1 = datetime.date(year1, month1, day1)
x4 = (date1 - date).days * 24 * 60 * 60
print(x4)
