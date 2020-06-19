# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

def convert_to_day(x):
    m, d, y = map(int, x.split())
    day = calendar.weekday(y, m , d)
    print(calendar.day_name[day].upper())

convert_to_day(input())