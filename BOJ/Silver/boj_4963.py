# [백준] 그래프 탐색 > 섬의 개수

# dfs 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)

def bfs(x, y, answer) :
    if not (0 <= x < w and 0 <= y < h) :
        return
    if graph[y][x] == 1 :
        graph[y][x] = answer
        bfs(x, y-1, answer) # 위
        bfs(x+1, y-1, answer) # 오른쪽 위
        bfs(x+1, y, answer) # 오른쪽
        bfs(x+1, y+1, answer) # 오른쪽 아래
        bfs(x, y+1, answer) # 아래
        bfs(x-1, y+1, answer) # 왼쪽 아래
        bfs(x-1, y, answer) # 왼쪽
        bfs(x-1, y-1, answer) # 왼쪽 위
        return True
    return False


while True :
    w, h = map(int, input().split())
    if w + h == 0 : break

    graph = []
    for _ in range(h) :
        graph.append(list(map(int, input().split())))

    answer = -1
    for col in range(w) :
        for row in range(h) :
            if graph[row][col] == 1 :
                if bfs(col, row, answer) :
                    answer -= 1
    print(-answer-1)

# bfs 풀이
# 시간초과 났었는데 큐에 넣으면서 바로 방문처리를 해줌으로써 해결
# import sys
# input = sys.stdin.readline
# from collections import deque

# while True :
#     w, h = map(int, input().split())
#     if w + h == 0 : break

#     graph = []
#     for _ in range(h) :
#         graph.append(list(map(int, input().split())))

#     q = deque()
#     answer = 0
#     for col in range(w) :
#         for row in range(h) :
#             if graph[row][col] == 1 :
#                 q.append((col, row))
#                 answer -= 1
#                 graph[row][col] = answer # 이 부분과
#                 while q :
#                     x, y = q.popleft()
#                     graph[y][x] = answer
#                     dx = [0, 1, 1, 1, 0, -1, -1, -1]
#                     dy = [-1, -1, 0, 1, 1, 1, 0, -1]
#                     for i in range(8) :
#                         nx = x + dx[i]
#                         ny = y + dy[i]
#                         if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1 :
#                             q.append((nx, ny))
#                             graph[ny][nx] = answer # 이 부분이 없으면 시간 초과

#     print(-answer)

