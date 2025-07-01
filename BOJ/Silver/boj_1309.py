# [백준] 다이나믹 프로그래밍 > 동물원

import sys
input = sys.stdin.readline

n = int(input())

dp = [1, 1, 1]
for row in range(1, n) :
    dp =[sum(dp), dp[0]+dp[2], dp[0]+dp[1]]

print(sum(dp) % 9901)