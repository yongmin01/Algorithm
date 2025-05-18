# [백준] 그래프 이론 > 토마토

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = []
for h in range(H) :
    twodimention = []
    for r in range(N) :
        twodimention.append(list(map(int, input().split())))
    graph.append(twodimention)

q = deque()
for h in range(H) :
    for r in range(N) :
        for c in range(M) :
            if graph[h][r][c] == 1 :
                q.append((h, r, c, 1))


while q :
    h, x, y, day= q.popleft()
    graph[h][x][y] = day # 이 코드가 없어도 정답이라서 지웠는데 오히려 시간, 메모리를 더 사용함.. 왜지?
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]
    for d in range(6) :
        nx = x + dx[d]
        ny = y + dy[d]
        nz = h + dh[d]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][nx][ny] == 0 :
            q.append((nz, nx, ny, day+1))
            graph[nz][nx][ny] = day+1

answer = 0
for h in range(H) :
    for r in range(N) :
        for c in range(M) :
            if graph[h][r][c] == 0 :
                print(-1)
                exit()
            else :
                answer = graph[h][r][c] if graph[h][r][c] > answer else answer
print(answer-1)