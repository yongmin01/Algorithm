# [백준] DP > 연속합

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
enum = []

if arr[0] < 0 :
    enum.append(0)
else :
    enum.append(arr[0])

for i in range(1, n) :
    if  -arr[i] > enum[i-1] :
        enum.append(0)
    else : enum.append(enum[i-1] + arr[i])
print(enum)
MAX = max(enum)
print(MAX if MAX > 0 else max(arr))