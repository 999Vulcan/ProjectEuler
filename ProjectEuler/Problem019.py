"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def leapYear(y):
    return True if y%400 == 0 or (y%4 == 0 and y%100 != 0) else False

def yearLength(y):
    return 366 if leapYear(y) else 365

def monthLength(m, y):
    if m == 2:
        return 29 if leapYear(y) else 28
    return 30 if m in [4,6,9,11] else 31

def dayOfYear(d, m, y):
    n = 0
    for month in range(1, m):
        n += monthLength(month, y)
    return n + d

def dayNumber(d, m, y):
    n = 0
    for year in range(1900, y):
        n += yearLength(year)
    return n + dayOfYear(d, m, y)

sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if dayNumber(1, month, year) % 7 == 0:
            sundays += 1

print(sundays)
