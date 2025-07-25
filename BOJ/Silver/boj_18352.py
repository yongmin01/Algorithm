# [백준] 최단경로 > 특정 거리의 도시 찾기

import sys
input = sys.stdin.readline
import heapq

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m) :
    st, ed = map(int, input().split())
    graph[st].append(ed)

distance = [-1 for _ in range(n+1)]
q = []
heapq.heappush(q, (0, x))
while q :
    dist, v = heapq.heappop(q)
    for i in graph[v] :
        if distance[i] == -1 :
            distance[i] = dist+1
            heapq.heappush(q, (dist+1, i))

answer = []
for i in range(1, n+1) :
    if distance[i] == k and i != x :
        answer.append(i)
if len(answer) > 0 :
    for i in answer : print(i)
else : print(-1)