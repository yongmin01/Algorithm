# 백준_DP : 동전 2

import sys
import math

input = sys.stdin.readline
n, k = map(int, input().split())
coins = set()
for i in range(n) :
    coins.add(int(input()))

INF = math.inf
dp = [INF] * (k+1)
dp[0] = 0
for coin in coins :
    for i in range(coin, k+1) :
        dp[i] = min(dp[i], dp[i - coin]+1)

if dp[k] == INF : print(-1)
else : print(dp[k])