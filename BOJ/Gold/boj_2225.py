# [백준] DP > 합분해

n, k = map(int, input().split())
dp = [[1 for _ in range(n+1)] for _ in range(k+1)]

for i in range(1, k+1) :
    dp[i][0] = 1

for i in range(2, k+1) :
    for l in range(1, n+1) :
        dp[i][l] = dp[i-1][l] + dp[i][l-1]

        

print(dp[-1][-1] % 1000000000)
