# 백준_BFS : 쉬운 최단거리

import sys
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())

graph = []
for c in range(n) :
    r = list(map(int, input().split()))
    if 2 in r :
        start = (c, r.index(2))
    graph.append(r)

queue = deque()
queue.append(start)

# 각 지점까지의 거리를 0으로 초기화
distance = [[0 for c in range(m)] for r in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while queue :
    x, y = queue.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if  graph[nx][ny] == 1 and graph[nx][ny] != 2 :
                if distance[nx][ny] == 0 : 
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

# 원래 갈 수 있는 곳인데 못 가게 된 곳에 -1 채우기
for r in range(n) :
    for c in range(m) :
        if graph[r][c] == 1 and distance[r][c] == 0 :
            distance[r][c] = -1

for r in range(n) :
    print(*distance[r])

