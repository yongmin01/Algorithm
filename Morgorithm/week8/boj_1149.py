# 백준_DP : RGB거리

import sys
input = sys.stdin.readline

cost = []

N = int(input())
for i in range(N) :
    temp = list(map(int, input().split()))
    cost.append(temp)

for i in range(1, N) :
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[N-1]))