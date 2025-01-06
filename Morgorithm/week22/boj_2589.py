# 백준_브루트포스 알고리즘 : 보물섬

import sys
from collections import deque

input = sys.stdin.readline
Length, Width = map(int, input().split())
graph = []
queue = deque()

for l in range(Length) :
    row = input().rstrip()
    graph.append(row)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def getDistance(r, c) :
    visited = [[-1 for _ in range(Width)] for _ in range(Length)]
    visited[r][c] = 0
    while queue :
        [x, y] = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < Length and 0 <= ny < Width) :
                if graph[nx][ny] == 'L' and visited[nx][ny] == -1 :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
    max = 0
    for r in range(Length) :
        for c in range(Width) :
            if visited[r][c] > max :
                max = visited[r][c]
    return max

answer = 0
for r in range(Length) :
    for c in range(Width) :
        if graph[r][c] == 'L' :
            queue.append([r, c])
            temp = getDistance(r, c)
            if temp > answer : 
                answer = temp
print(answer)