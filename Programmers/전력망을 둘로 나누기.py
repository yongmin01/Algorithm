# [프로그래머스] 완전탐색 > 전력망을 둘로 나누기

# Union-Find를 이용한 풀이
from collections import Counter

def solution(n, wires):
    answer = n
    
    def find(x) :
        if parents[x] != x :
            parents[x] = find(parents[x])
        return parents[x]

    def union(a, b) :
        a = find(a)
        b = find(b)
        if a != b :
            if a < b : parents[b] = a
            else : parents[a] = b

    
    for x in wires :
        parents = [i for i in range(n+1)]
        for wire in wires :
            if wire != x :
                union(wire[0], wire[1])
        
        # 모든 노드의 루트를 갱신
        for i in range(1, n+1) : find(i)
        
        c = Counter(parents[1:])
        c_values = list(c.values())
        answer = min(answer, abs(c_values[0] - c_values[1]))
    
    return answer

# BFS를 이용한 풀이
from collections import deque

def solution(n, wires):
    answer = n
    
    # 그래프 만들기
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires :
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    q = deque()
    for v1, v2 in wires :
        # 간선 제거
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        # BFS
        visited = [False for _ in range(n+1)]
        q.append(1)
        visited[1] = True
        while q :
            curr = q.popleft()
            for v in graph[curr] :
                if not visited[v] :
                    visited[v] = True
                    q.append(v)
                    
        group1 = visited.count(True)
        group2 = n - group1
        answer = min(answer, abs(group1-group2))
        
        # 간선 다시 추가
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return answer
