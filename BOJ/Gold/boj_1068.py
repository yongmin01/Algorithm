# [백준] DFS > 트리

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(51)

n = int(input())
nodes = list(map(int, input().split()))
target = int(input())

graph = [[] for _ in range(n)]
leaf = 0
for i in range(n) :
    if nodes[i] != -1 :
        graph[nodes[i]].append(i)
for node in graph :
    if len(node) == 0 : leaf += 1

delete = 0

def dfs(v) :
    global delete
    if len(graph[v]) == 0 :
        if len(graph[nodes[v]]) != 1 :
            delete += 1
        return
    for i in graph[v] :
        dfs(i)

if nodes[target] == -1 :
    print(0)
else :
    dfs(target)
    print(leaf - delete)