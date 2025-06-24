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

# 루트 노드에서 가장 먼 노드 찾기
visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
visited[1] = True
dfs(1)

max_v = distance.index(max(distance))

# 찾은 노드에서 가장 먼 노드 찾기
visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
visited[max_v] = True
dfs(max_v)

print(max(distance))


# 다익스트라 풀이 => 메모리 초과

# import sys
# input = sys.stdin.readline
# import heapq
# from itertools import combinations

# n = int(input())

# tree = [[] for _ in range(n+1)]
# parents = set()
# for _ in range(n-1) :
#     p, c, w = map(int, input().split())
#     parents.add(p)
#     tree[p].append((c, w))
#     tree[c].append((p, w))

# leaves = set(i for i in range(1, n+1)) - parents
# comb = list(combinations(leaves, 2))


# def dijkstra(start) :
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q :
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist :
#             continue
#         for i in tree[now] :
#             cost = dist + i[1]
#             if cost < distance[i[0]] :
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# INF = int(1e9)
# answer = 0
# for i in comb:
#     distance = [INF] * (n+1)
#     dijkstra(i[0])
#     if distance[i[1]] > answer :
#         answer = distance[i[1]]

# print(answer)