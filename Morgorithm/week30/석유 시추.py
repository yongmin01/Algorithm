# [프로그래머스] PCCP 기출문제 2번 > 석유 시추

from collections import deque

def solution(land):
    queue = deque()
    land_group = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    
    def bfs (queue, g) :
        while queue :
            [x, y] = queue.popleft()
            
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for d in range(4) :
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < len(land) and 0 <= ny < len(land[0]) :
                    if land[nx][ny] and land_group[nx][ny] == 0 :
                        queue.append([nx, ny])
                        land_group[nx][ny] = g # 방문 체크
                        group[-1] += 1
    
    # 석유 덩어리 만들기 (덩어리 이름(g)은 1부터 시작)
    g = 1
    group = [0]
    for r in range(len(land)) :
        for c in range(len(land[0])) :
            if (land[r][c] != 0) and (land_group[r][c] == 0) :
                group.append(1)
                queue.append([r, c])
                land_group[r][c] = g
                bfs(queue, g)
                g += 1
    
    answer = 0
    for c in range(len(land[0])) :
        get = set()
        for r in range(len(land)) :
            if land_group[r][c] != 0 :
                get.add(land_group[r][c])
        oil = 0
        for a in list(get) :
            oil += group[a]
        if answer < oil :
            answer = oil
    return answer