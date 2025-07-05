# [백준] 그래프 탐색, 최단 경로 > 나이트의 이동

import sys
input = sys.stdin.readline
from collections import deque


testcase = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
for _ in range(testcase) :
    l = int(input())
    startX, startY = map(int, input().split())
    targetX, targetY = map(int, input().split())
    q = deque()
    q.append((startX, startY, 0))
    

    visited = [[0 for _ in range(l)] for _ in range(l)]
    visited[startX][startY] = -1

    while q :
        currX, currY, distance = q.popleft()
        if currX == targetX and currY == targetY :
            print(distance)
            break
        distance += 1
        for i in range(8) :
            nx = currX + dx[i]
            ny = currY + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0 :
                visited[nx][ny] = distance
                q.append((nx, ny, distance))

        