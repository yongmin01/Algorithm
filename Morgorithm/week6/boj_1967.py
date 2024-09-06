# 백준_트리 & 깊이 우선 탐색 : 트리의 지름

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

stack = []
n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1) :
    parent, child, weight = list(map(int, input().split()))
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])

visited = [-1 for _ in range(n+1)]
visited[1] = 0
def dfs(parent, distance) :
    for node in tree[parent] :
        new_distance = distance + node[1]
        if visited[node[0]] == -1:
            visited[node[0]] = new_distance
            dfs(node[0], new_distance)
dfs(1, 0)
max_distande = visited.index(max(visited))

visited = [-1 for _ in range(n+1)]
visited[max_distande] = 0
dfs(max_distande, 0)
print(max(visited))