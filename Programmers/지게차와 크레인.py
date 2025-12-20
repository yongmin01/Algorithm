# [프로그래머스] 지게차와 크레인

from collections import deque

def solution(storage, requests):
    storage = [list(map(str, storage[i])) for i in range(len(storage))]
    
    def bfs(x, y, rows, columns) : # 현재 컨테이너가 접근 가능한 컨테이너인지 바깥으로 뻗어나가며 확인
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        visited[x][y] = True
        
        q = deque()
        q.append([x, y])
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        while q :
            x, y = q.popleft()
            for i in range(4) :
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < rows and 0 <= ny < columns :
                    if storage[nx][ny] == 0 and not visited[nx][ny] :
                        q.append([nx, ny])
                        visited[nx][ny] = True
                else :
                    return True
        return False
    
    answer = 0
    rows, columns = len(storage), len(storage[0])
    for request in requests :
        if len(request) == 1 : # 지게차 이용
            order = request[0]
            temp = []
            for r in range(rows) :
                for c in range(columns) :
                    if storage[r][c] == order :
                        if bfs(r, c, rows, columns) :
                            temp.append([r, c])
            for x, y in temp : # 꺼냄 처리
                storage[x][y] = 0
                answer += 1
                
        else : # 크레인 사용
            order = request[0]
            for r in range(rows) :
                for c in range(columns) :
                    if storage[r][c] == order : # 요청과 일치하는 컨테이너 즉시 꺼냄 처리(0)
                        storage[r][c] = 0
                        answer += 1
            
            
    return rows*columns - answer