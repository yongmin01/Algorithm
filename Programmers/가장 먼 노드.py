# [프로그래머스] 그래프 > 가장 먼 노드

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    q.append(1)
    
    distance = [-1 for _ in range(n+1)]
    
    distance[1] = 0
    while q :
        curr = q.popleft()
        for v in graph[curr] :
            if distance[v] == -1 :
                distance[v] = distance[curr] + 1
                q.append(v)
    
    return distance.count(max(distance[2:]))
    