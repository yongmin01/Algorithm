# [프로그래머스] > 부대복귀

import heapq

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for road in roads :
        st, en = road
        graph[st].append(en)
        graph[en].append(st)
    
    INF = int(1e9)
    distance = [INF for _ in range(n+1)]
    distance[destination] = 0
    q = []
    heapq.heappush(q, (0, destination))
    while q :
        dist, v = heapq.heappop(q)
        if distance[v] < dist :
            continue
        for i in graph[v] :
            if distance[i] > dist :
                distance[i] = dist + 1
                heapq.heappush(q, (dist+1, i))
    
    for source in sources :
        answer.append(distance[source] if distance[source] != INF else -1)
        
    
    return answer