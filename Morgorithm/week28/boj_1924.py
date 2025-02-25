# 백준_구현 : 2007년

import sys
input = sys.stdin.readline

x, y = map(int, input().split())

days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_of_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

day = 0

for m in range(x) :
    day += days_of_month[m]
day += y
print(days_of_week[day % 7])