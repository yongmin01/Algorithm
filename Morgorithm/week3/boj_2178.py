# 백준 너비 우선 탐색 : 미로 탐색

import sys
from collections import deque

input = sys.stdin.readline

[N, M] = map(int, input().split())

graph = []
for i in range(N) :
    graph.append(list(map(int, ''.join(input().split()))))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append((0, 0))

while queue :
    x, y = queue.popleft()

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M :
            if graph[nx][ny] == 1 :
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

print(graph[N-1][M-1])