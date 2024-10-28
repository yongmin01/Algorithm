# 백준_MST : 최소 스패닝 트리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

V, E = map(int, input().split())
edges = []
parent = [x for x in range(V+1)]
result = 0

def find_parent(n) :
    if parent[n] != n :
        parent[n] = find_parent(parent[n])
        return parent[n]
    return n

for i in range(E) :
    edges.append(list(map(int, input().split())))
edges.sort(key= lambda x : x[2])

for edge in edges :
    n1 = edge[0]
    n2 = edge[1]
    p1 = find_parent(n1)
    p2 = find_parent(n2)
    if p1 == p2 : continue
    else :
        parent[p1] = p2
        result += edge[2]
        
print(result)