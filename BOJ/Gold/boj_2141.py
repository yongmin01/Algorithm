# [백준] 그리디 > 우체국

import sys
input = sys.stdin.readline

n = int(input())
arr = []
total = 0
for _ in range(n) :
    x, a = map(int, input().split())
    arr.append([x, a])
    total += a
arr.sort()

answer = arr[0][0]
location = 0
population = arr[location][1]

while population < (total+1) // 2 :
    location += 1
    population += arr[location][1]

print(arr[location][0])