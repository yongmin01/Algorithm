# 백준_DP : 계단 오르기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stairs = deque(int(input()) for _ in range(n))
stairs.appendleft(0)

dp = [0 for _ in range(n+1)]
dp[1] = stairs[1]

if n == 1 :
    print(dp[1])
elif n == 2 :
    dp[2] = stairs[1] + stairs[2] 
    print(dp[2])
elif n == 3 :
    dp[2] = stairs[1] + stairs[2] 
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    print(dp[3])
else :
    dp[2] = stairs[1] + stairs[2] 
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    for i in range(4, n+1) :
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
    print(dp[n])

