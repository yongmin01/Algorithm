# [백준] 다익스트라 > 최소비용 구하기

import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

start, target = map(int, input().split())

INF = 1e9
cities = [INF for _ in range(n+1)]

pq = []
cities[start] = 0
heapq.heappush(pq, [0, start])
while pq :
    w, cur = heapq.heappop(pq)
    if cities[cur] < w : continue # 이미 방문한 경우는 스킵하기!! if curr == target : break로 미리 종료해버리는건 오답 위험 있음
    for end, cost in graph[cur] :
        if cities[end] > w + cost :
            cities[end] = w + cost
            heapq.heappush(pq, [cities[end], end])
    
print(cities[target])
