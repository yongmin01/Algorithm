# [백준] DFS > 트리의 지름

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
tree = [[] for _ in range(n+1)]

for i in range(n-1) :
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

def dfs(v) :
    for i in tree[v] :
        if not visited[i[0]] :
            visited[i[0]] = True
            distance[i[0]] = distance[v] + i[1]
            dfs(i[0])

visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
visited[1] = True
dfs(1)

max_v = distance.index(max(distance))

visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
visited[max_v] = True
dfs(max_v)

print(max(distance))