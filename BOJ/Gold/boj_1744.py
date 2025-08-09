# [백준] 그리디, 정렬 > 수 묶기

import sys
input = sys.stdin.readline

n = int(input())
neg = []
pos = []
for _ in range(n) :
    num = int(input())
    if num > 0 : pos.append(num)
    else : neg.append(num)

neg.sort()
pos.sort(reverse=True)

sum = 0
prev = False

# 음수 2개 짝지어서 곱하고 더하기
for i in neg :
    if prev is False :
        prev = i
    else :
        sum += prev * i
        prev = False

if prev is not False :
    sum += prev
    prev = False

# 양수2개 짝지어서 곱하고 더하기
# 이때 1은 곱하지 않고 더함
for i in pos :
    if prev is False :
        prev = i
    else :
        if i == 1 :
            sum += 1
            sum += prev
            prev = False
        else : 
            sum += prev * i
            prev = False

if prev is not False :
    sum += prev

print(sum)
