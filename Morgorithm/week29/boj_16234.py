# 백준_시뮬레이션, BFS : 인구 이동
# BFS로도 풀어보기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)

N, L, R = map(int, input().split())

graph = []
for r in range(N) :
    graph.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(r, c, union) :
    visited[r][c] = True
    for d in range(4) :
        ny = r + dy[d]
        nx = c + dx[d]
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
            if abs(graph[ny][nx] - graph[r][c]) in range(L, R+1) :
                union.add((r, c))
                union.add((ny, nx))
                dfs(ny, nx, union)
    return union

answer = 0
while True :
    visited = [[False for _ in range(N)] for _ in range(N)]
    unions = []
    for r in range(N) :
        for c in range(N) :
            if not visited[r][c] :
                union = dfs(r, c, set())
                if len(list(union)) != 0 :
                    unions.append(union)
    if len(unions) == 0 : 
        print(answer)
        break
    else :
        answer += 1
        for union in unions :
            list_union = list(union)
            sum = 0
            newPopulation = 0
            for country in list_union :
                sum += graph[country[0]][country[1]]

            newPopulation = sum // len(list_union)
            for country in list_union :
                graph[country[0]][country[1]] = newPopulation