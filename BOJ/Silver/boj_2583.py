# [백준] 그래프 이론 > 영역 구하기

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

M, N, K = map(int, input().split())
# 0은 칠해져서 갈 수 없는 곳, 1은 갈 수 있는 곳
graph = [[1 for _ in range(N)] for _ in range(M)]

for area in range(K) :
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2) :
        for c in range(x1, x2) :
            graph[M-1-r][c] = 0

def dfs(x, y) :
    global a
    if x < 0 or x >= N or y < 0 or y >= M :
        return 0
    if graph[y][x] == 1 :
        graph[y][x] = 'v'
        a += 1
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        return a
    return 0

area = []
for x in range(N) :
    for y in range(M) :
        if graph[y][x] == 1 :
            a = 0
            area.append(dfs(x, y))

print(len(area))
area.sort()
print(' '.join(map(str, area)))
