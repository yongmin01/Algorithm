# [프로그래머스] 2024 KAKAO WINTER INTERNSHIP > 도넛과 막대 그래프

def solution(edges):
    answer = [0, 0, 0, 0]
    MAX = 1000000
    come_in = [0 for _ in range(MAX+1)]
    graph = [[] for _ in range(MAX+1)]
    nodes = [False for _ in range(MAX+1)]
    
    for edge in edges :
        a, b = edge
        nodes[a] = True
        nodes[b] = True
        come_in[b] += 1
        graph[a].append(b)
    
    fake = 0
    for v in range(1, MAX+1) : # 생성한 정점 찾기
        if len(graph[v]) > 2 :
            fake = v
            break
        if len(graph[v]) == 2 and come_in[v] == 0 :
            fake = v
            break
    answer[0] = fake
    
    for v in range(1, MAX+1) :
        if v != fake :
            if len(graph[v]) == 2 : # 8자모양 그래프는 나가는 간선이 2개
                answer[3] += 1
            elif len(graph[v]) == 0 and nodes[v]: # 막대 그래프는 나가는 간선이 0개
                answer[2] += 1
    # 도넛 모양 그래프는 (추가한 정점에서 나가는 간선 개수) - (나머지 두 종료의 그래프 개수)
    answer[1] = len(graph[fake]) - answer[2] - answer[3] 
    
    return answer