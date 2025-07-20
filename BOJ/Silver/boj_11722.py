# [백준] DP > 가장 긴 감소하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for start in range(1, n) :
    temp = 0
    for back in range(start - 1, -1, -1) :
        if arr[back] > arr[start] :
            if dp[back] > temp :
                temp = dp[back]
        if back == 0 :
            dp[start] = temp + 1

print(max(dp))