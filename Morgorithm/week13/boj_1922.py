# 백준_MST : 네트워크 연결

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
M = int(input())
parent = [x for x in range(N + 1)]
edges = []
result = 0

for i in range(M) :
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x : x[2])

def find_parent(n) :
    if parent[n] != n :
        parent[n] = find_parent(parent[n])
        return parent[n]
    return n

for edge in edges :
    n1, n2 = edge[0], edge[1]
    p1, p2 = find_parent(n1), find_parent(n2)
    if p1 == p2 : continue
    else :
        parent[p1] = p2
        result += edge[2]

print(result)