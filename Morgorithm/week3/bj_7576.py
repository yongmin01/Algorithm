# 백준_너비 우선 탐색 : 토마토

import sys
input = sys.stdin.readline
from collections import deque
queue = deque()

M, N = map(int, input().split())
graph = []
for y in range(N) :
    row = list(map(int, input().split()))
    for x in range(M) :
        if row[x] == 1 :
            queue.append((x, y))
    graph.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue :
    x, y = queue.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:

            if graph[ny][nx] == 0 :
                queue.append((nx, ny))
                graph[ny][nx] = graph[y][x] + 1

max = 0             
for y in range(N) :
    for x in range(M) :
        if graph[y][x] == 0 :
            print(-1)
            exit()
        if graph[y][x] >= max :
            max = graph[y][x]
if (max == 1) : print(0) # 이미 다익어있는 경우
else : print(max-1) # 정상적인 경우





