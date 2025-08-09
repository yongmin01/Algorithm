# [백준] 다익스트라 > 최단경로

import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())

k = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e) :
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

INF = int(1e9)
distance = [INF for _ in range(v+1)]
distance[k] = 0

pq = []

heapq.heappush(pq, (0, k))

while pq :
    dis, node = heapq.heappop(pq)
    if distance[node] < dis :
        continue
    for i, weight in graph[node] :
        if dis+weight < distance[i] : 
            distance[i] = dis+weight
            heapq.heappush(pq, (dis+weight, i))

for i in range(1, v+1) :
    print(distance[i] if distance[i] != INF else "INF")