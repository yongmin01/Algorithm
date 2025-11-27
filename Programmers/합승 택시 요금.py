# [프로그래머스] 합승 택시 요금

import heapq
def solution(n, s, a, b, fares):
    answer = int(2e9)
    
    graph = [[] for _ in range(n+1)]
    for v1, v2, w in fares :
        graph[v1].append([w, v2])
        graph[v2].append([w, v1])
    def dijikstra(s) :
        pq = []
        visited = [False for _ in range(n+1)]
        distance = [int(2e9) for _ in range(n+1)]
        distance[s] = 0
        visited[s] = True
        heapq.heappush(pq, (0, s))

        while pq :
            weight, curr = heapq.heappop(pq)
            if distance[curr] < weight : continue
            for w, v in graph[curr] :
                if weight + w < distance[v] :
                    heapq.heappush(pq, (weight+w, v))
                    distance[v] = weight + w
        return distance
    
    ds = dijikstra(s)
    da = dijikstra(a)
    db = dijikstra(b)
    
    for i in range(n+1) :
        answer = min(answer, ds[i]+da[i]+db[i])
    return answer