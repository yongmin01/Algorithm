# 백준 너비 우선 탐색 & 깊이 우선 탐색 : 연결 요소의 개수

import sys
input = sys.stdin.readline
from collections import deque


[N, M] = map(int, input().split())

edges = []
connected = [[] for _ in range(N+1)]
for i in range(M) :
    [a, b] = (map(int, input().split()))
    connected[a].append(b)
    connected[b].append(a)

def dfs(queue) :
    while queue :
        curr = queue.popleft()
        for i in connected[curr] :
            if not visited[i] : 
                visited[i] = True
                queue.append(i)

visited = [False for _ in range(N+1)]
result = 0
queue = deque()
for v in range(1, N+1) :
    if not visited[v] : 
        visited[v] = True
        result += 1
        queue.append(v)
        dfs(queue)
print(result)


        

