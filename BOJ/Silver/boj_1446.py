# [백준] DP > 지름길

import sys
input = sys.stdin.readline
from collections import defaultdict

n, d = map(int, input().split())
roads = defaultdict(list)

for _ in range(n) :
    s, e, dis = map(int, input().split())
    if e - s <= dis : continue
    else : 
        roads[e].append([s, dis])


dp = [0 for _ in range(d+1)]
for i in range(1, d+1) :
    dp[i] = dp[i-1] + 1
    if i in roads.keys() :
        for road in roads[i] :
            dp[i] = min(dp[i], dp[road[0]] + road[1])

print(dp[d])