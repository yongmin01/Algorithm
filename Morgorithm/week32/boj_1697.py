# 백준_너비 우선 탐색 : 숨바꼭질

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

visited = [0 for _ in range(200001)]
queue = deque()
queue.append((N, 0))
def bfs() :
    while queue :
        curr, step = queue.popleft()
        if curr == K :
            return step
        visited[curr] = 1
        if 0 <= curr - 1 and not visited[curr - 1] :
            queue.append((curr - 1, step + 1))
        if curr + 1 < 200001 and not visited[curr + 1] :
            queue.append((curr + 1, step + 1))
        if curr * 2 < 200001 and not visited[curr * 2] :
            queue.append((curr * 2, step + 1))

print(bfs())


