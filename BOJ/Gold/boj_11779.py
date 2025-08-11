# [백준] 다익스트라, 역추적 > 최소비용 구하기 2

import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

A, B = map(int, input().split())

pq = []
dis = [1000000000 for _ in range(n+1)]
prevNode = [i for i in range(n+1)]
heapq.heappush(pq, (0, A))
while pq :
    w, node = heapq.heappop(pq)
    if dis[node] < w : continue

    for n in graph[node] :
        v, weight = n
        cost = w + weight
        if cost < dis[v] :
            prevNode[v] = node
            dis[v] = cost
            heapq.heappush(pq, (cost, v))

now = B
answer = []
answer.append(B)
while now != A :
    answer.append(prevNode[now])
    now = prevNode[now]

print(dis[B])
print(len(answer))
for i in answer[::-1] :
    print(i, end=" ")