# [백준] MST > 최소 스패닝 트리

# Kruskal 풀이

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
v, e = map(int, input().split())

edges = []
for _ in range(e) :
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x : x[2])

parent = [i for i in range(v+1)]

def find_parent(x) :
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(parent, a, b) :
    a = find_parent(a)
    b = find_parent(b)
    if a < b : parent[b] = a
    else : parent[a] = b

ans = 0
for edge in edges :
    v1, v2, w = edge
    if find_parent(v1) != find_parent(v2) :
        union(parent, v1, v2)
        ans += w
    else : continue

print(ans)

# ---

# Prim 풀이

import sys
import heapq

input = sys.stdin.readline
v, e = map(int, input().split())

pq = []

graph = [[] for _ in range(v+1)]
for _ in range(e) :
    v1, v2, w = map(int, input().split())
    graph[v1].append([w, v2])
    graph[v2].append([w, v1])

for edge in graph[1] :
    heapq.heappush(pq, edge)

visited = [False for _ in range(v+1)]
visited[1] = True

ans = 0
while pq :
    w, v = heapq.heappop(pq)
    if visited[v] : continue
    else :
        visited[v] = True
        ans += w
        for edge in graph[v] :
            heapq.heappush(pq, edge)

print(ans)
