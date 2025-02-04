# 백준_DP : 사회망 서비스(SNS)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)] # [내가 얼리어답터 X, 내가 얼리어답터 O]

for _ in range(N-1) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)

def dfs(v) :
    visited[v] = True
    print(visited)
    for child in graph[v] :
        if not visited[child] :
            dfs(child)
            dp[v][0] += dp[child][1]
            dp[v][1] += min(dp[child][0], dp[child][1])
    dp[v][1] += 1
    print(dp)

dfs(1)
print(min(dp[1][0], dp[1][1]))
    