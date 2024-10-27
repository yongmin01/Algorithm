# 백준_mst: 집합의 표현

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int ,input().split())

graph = [x for x in range(n+1)]

def find(n) :
    if graph[n] != n :
        graph[n] = find(graph[n])
        return graph[n]
    return n
def union(n1, n2) :
    p1 = find(n1)
    p2 = find(n2)
    graph[p1] = p2

for i in range(m) :
    o, a, b = map(int, input().split())
    if o == 0 :
        if a == b : continue
        else : union(a, b)

    if o == 1 :
       if find(a) == find(b) : print("YES")
       else :
           print("NO")

