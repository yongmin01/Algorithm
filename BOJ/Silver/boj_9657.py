# [백준] DP > 돌 게임 3

N = int(input())
dp = [0] * (N+1)

if N >= 1 :
    dp[1] = 'SK'
if N >= 2 :
    dp[2] = 'CY'
if N >= 3 :
    dp[3] = 'SK'
if N >= 4 :
    dp[4] = 'SK'

if N <= 4 :
    print(dp[N])
else :
    for i in range(5, N+1) :
        if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY' :
            dp[i] = 'SK'
        else : dp[i] = 'CY'
    print(dp[N])