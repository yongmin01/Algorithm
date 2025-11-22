# [백준] DP > LCS

import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
n, m = len(s1), len(s2)
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1 if s1[0] == s2[0] else 0
for i in range(1, n) :
    if s1[i] == s2[0] : dp[i][0] = 1
    else : dp[i][0] = dp[i-1][0]
for l in range(1, m) :
    if s1[0] == s2[l] : dp[0][l] = 1
    else : dp[0][l] = dp[0][l-1] 

for i in range(1, n) :
    for l in range(1, m) :
        if s1[i] == s2[l] :
            dp[i][l] = dp[i-1][l-1] + 1
        else :
            dp[i][l] = max(dp[i-1][l], dp[i][l-1])

print(dp[n-1][m-1])