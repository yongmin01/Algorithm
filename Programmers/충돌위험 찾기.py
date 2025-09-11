# [프로그래머스] PCCP 기출문제 3번 > 충돌위험 찾기

from collections import defaultdict

def solution(points, routes):
    answer = 0
    
    # 각 로봇의 최단 경로 구하기
    shortest_path = [[] for _ in range(len(routes))]
    for i in range(len(routes)) :
        route = routes[i]
        sx, sy = points[route[0]-1]
        shortest_path[i].append([sx, sy])
        
        for point in route[1:] :
            dx, dy = points[point-1]
            while True :
                if sx < dx : # 아래로 이동해야 하는 경우
                    sx = sx + 1
                    shortest_path[i].append([sx, sy])
                elif sx > dx : # 위로 이동해야 하는 경우
                    sx = sx - 1
                    shortest_path[i].append([sx, sy])
                else : 
                    if sy < dy : # 오른쪽으로 이동해야 하는 경우
                        sy = sy + 1
                        shortest_path[i].append([sx, sy])
                    elif sy > dy : # 왼쪽으로 이동해야 하는 경우
                        sy = sy - 1
                        shortest_path[i].append([sx, sy])
                    else : # 지점에 도착한 경우
                        break
    
    # 최단 경로가 제일 길어서 가장 긴 시간을 움직여야 하는 로봇(순회할 시간의 최댓값 구하기)
    max_time = max(len(shortest_path[route]) for route in range(len(shortest_path)))
    for time in range(max_time) :
        time_dict = defaultdict(int) # 해당 초에 모든 로봇의 위치를 담는 딕셔너리
        for i in range(len(shortest_path)) :
            route = shortest_path[i]
            if len(route) - 1 >= time : # 해당 로봇의 경로가 현재 시간보다 길어서 아직 방문할 지점이 남은 경우(운송이 끝나지 않은 경우)
                time_dict[tuple(route[time])] += 1 
                if time_dict[tuple(route[time])] == 2 : 
                    answer += 1
        
    return answer