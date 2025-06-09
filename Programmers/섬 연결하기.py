# [프로그래머스] 탐욕법(Greedy) : 섬 연결하기

def solution(n, costs):
    def find (parent, x) :
        if parent[x] != x :
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b) :
        a = find(parent, a)
        b = find(parent, b)
        
        if a < b : 
            parent[b] = a
        else :
            parent[a] = b
    
    parent = [0] * (n+1)
    for i in range(1, n+1) :
        parent[i] = i
    
    costs.sort(key= lambda x : x[2])
    
    answer = 0
    for cost in costs :
        e1, e2, c = cost
        if find(parent, e1) != find(parent, e2) :
            answer += c
            union(parent, e1, e2)
    
    return answer