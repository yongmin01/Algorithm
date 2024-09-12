# 백준_누적 합 & 두 포인터 : 부분합

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
sum = []

for i in range(N) :
    if i == 0 :
        sum.append(arr[i])
    else :
        sum.append(arr[i] + sum[i-1])
start = 0
end = 0
min = N + 1
while start <= end and end < N :
    temp = sum[end] - sum[start] + arr[start]
    if temp > S :
        if end-start+1 < min :
            min = end-start + 1
        start += 1
    elif temp < S :
        end += 1
    else :
        if end-start+1 < min :
            min = end-start + 1
        end += 1

if min == N + 1:
    print(0)
else :
    print(min)
