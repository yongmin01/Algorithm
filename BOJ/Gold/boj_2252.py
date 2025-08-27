# [백준] 위상 정렬 > 줄 세우기

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()

# 진입 차수가 0인 노드부터 탐색을 시작할 수 있도록 q에 삽입
for i in range(1, n+1) :
    if indegree[i] == 0 :
        q.append(i)

# 현재 노드에서 연결된 노드들의 진입 차수를 1씩 줄이고 0이 된다면 q에 삽입
answer = []
while q :
    curr = q.popleft()
    answer.append(curr)
    for i in graph[curr] :
        indegree[i] -= 1
        if indegree[i] == 0 : 
            q.append(i)

print(' '.join(list(map(str, answer))))