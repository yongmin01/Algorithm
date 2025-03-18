# 백준_브루트포스 : 외판원 순회 2

import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N) : 
    graph.append(list(map(int, input().split())))

def dfs(v) :
    global visited, distance
    visited[v] = 1
    if sum(visited) == N and graph[v][start_point] != 0 :
            costs.append(distance + graph[v][start_point])
            return
    for i in range(N) :
        if i != v and visited[i] == 0 and graph[v][i] != 0 :
            distance += graph[v][i]
            dfs(i)
            visited[i] = 0
            distance -= graph[v][i]
    return

costs= []
for v in range(N) : # v에서 출발하여 v로 돌아오는 방법들 순회
    visited = [0 for _ in range(N)]
    distance = 0
    start_point = v
    dfs(v)

print(min(costs))