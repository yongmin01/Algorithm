# [프로그래머스] 2022 KAKAO BLIND RECRUITMENT > 양과 늑대

def solution(info, edges):

    graph = [[] for _ in range(len(info))]
    for edge in edges :
        p, c = edge
        graph[p].append(c)
        
    max_sheep = 0
    wolf = 0
    total_sheep = info.count(0)
    
    def dfs(sheep, wolf, current, possible) :
        nonlocal max_sheep
        if info[current] == 0 :
            sheep += 1
        else : wolf += 1
        if wolf >= sheep : return
    
        max_sheep = max(max_sheep, sheep)
        if max_sheep == total_sheep : return max_sheep # 주어진 양을 모두 모았을 경우 바로 종료
        possible = possible.copy()
        possible.extend(graph[current])
        possible.remove(current)
        for n in possible :
            dfs(sheep, wolf, n, possible)
    
    dfs(0, 0, 0, [0])
        
    return max_sheep
