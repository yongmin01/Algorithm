# 백준_DP : 벼락치기

import sys
input = sys.stdin.readline

quiz_num, time_limit = map(int, input().split())
ests = [0]
values = [0]
for i in range(quiz_num) :
    est, value = map(int, input().split())
    ests.append(est)
    values.append(value)

dp = [[0 for i in range(quiz_num+1)] for i in range(time_limit+1)]

for q in range(1, quiz_num+1) :
    for t in range(1, time_limit+1) :
        if ests[q] > t : dp[t][q] = dp[t][q-1]
        else :
            dp[t][q] = max(values[q] + dp[t-ests[q]][q-1], dp[t][q-1])
        
print(dp[time_limit][quiz_num])