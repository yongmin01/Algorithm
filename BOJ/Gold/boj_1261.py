# [백준] 최단 경로, 0-1 BFS > 알고스팟

### 0-1 BFS를 이용한 풀이 ###

import sys
input = sys.stdin.readline
from collections import deque

q = deque()

n, m = map(int, input().split())
maze = []
INF = int(1e9)
visited = [[INF for _ in range(n)] for _ in range(m)]
for _ in range(m) :
    maze.append(list(map(int, input().strip())))


answer = n * m + 1

q.append((0, 0, 0))
visited[0][0] = 0
while q :
    x, y, bc = q.popleft()
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m and 0 <= ny < n) :
            if maze[nx][ny] == 1 :
                if visited[nx][ny] > bc + 1 :
                    visited[nx][ny] = bc + 1
                    q.append((nx, ny, bc + 1))
                else : continue
            else :
                if visited[nx][ny] > bc :
                    visited[nx][ny] = bc
                    q.appendleft((nx, ny, visited[nx][ny]))
                else : continue
            
print(visited[m-1][n-1])

# # 최적화 이전 - 0-1 BFS가 아닌 일반적인 BFS

# import sys
# input = sys.stdin.readline
# from collections import deque

# q = deque()

# n, m = map(int, input().split())
# maze = []
# INF = int(1e9)
# visited = [[INF for _ in range(n)] for _ in range(m)]
# for _ in range(m) :
#     maze.append(list(map(int, input().strip())))


# answer = n * m + 1

# q.append((0, 0, 0))
# visited[0][0] = 0
# while q :
#     x, y, bc = q.popleft()
    
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if (0 <= nx < m and 0 <= ny < n) :
#             if maze[nx][ny] == 1 :
#                 if visited[nx][ny] > bc + 1 :
#                     visited[nx][ny] = bc + 1
#                     q.append((nx, ny, bc + 1))
#                 else : continue
#             else :
#                 if visited[nx][ny] > bc :
#                     visited[nx][ny] = bc
#                     q.append((nx, ny, visited[nx][ny]))
#                 else : continue
            
# print(visited[m-1][n-1])


###.1차 시도 : DFS 풀이로 시간초과 (예제3 6*6일 때 10초 이상 소요됨) ###

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# maze = []
# visited = [[-1 for _ in range(n)] for _ in range(m)]
# for _ in range(m) :
#     maze.append(list(map(int, input().strip())))


# answer = n * m + 1
# def dfs(x, y, bc) :
#     global answer
#     if x == n-1 and y == m-1 :
#         if answer > bc :
#             answer = bc
#         # print(y, x, "is answer", answer)
#         return
    
#     if (not (0 <= x < n and 0 <= y < m)) :
#         # print(y, x, "returned!")
#         return
#     if visited[y][x] == -1 :
#         if maze[y][x] == 1 :
#             bc += 1
#         visited[y][x] = bc
#         # print(y, x, visited[y][x])

#         dfs(x, y-1, bc)
#         dfs(x+1, y, bc)
#         dfs(x, y+1, bc)
#         dfs(x-1, y, bc)
#         visited[y][x] = -1
    

# dfs(0, 0, 0)
# print(answer)


### 2차 시도 : BFS 풀이이지만 시간 초과 ###
# (해당 노드를 방문하기 위해 부셔야 할 방의 수가 현재 노드를 통해서 해당 노드로 가게 될 때 부셔야 하는 노드의 수보다 큰 경우만 방문하도록 했어야 함) #

import sys
input = sys.stdin.readline
from collections import deque

q = deque()

n, m = map(int, input().split())
maze = []
visited = [[-1 for _ in range(n)] for _ in range(m)]
for _ in range(m) :
    maze.append(list(map(int, input().strip())))


answer = n * m + 1

q.append((0, 0, 0))
visited[0][0] = 0
while q :
    x, y, bc = q.popleft()
    print("curr", x, y, bc)
    if x == m-1 and y == n-1 :
        if answer > bc :
            answer = bc
            print("ans update", answer)
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        print("nx:", nx, "ny:", ny)
        if not (nx == 0 and ny == 0) and 0 <= nx < m and 0 <= ny < n :
            if visited[nx][ny] == -1 :
                visited[nx][ny] = visited[x][y] + 1 if maze[nx][ny] == 1 else visited[x][y]
                q.append((nx, ny, visited[nx][ny]))
                print(x, "=>", nx, "/", y, "=>", ny, "appended/", visited[nx][ny])  

            elif visited[nx][ny] > visited[x][y] :
                visited[nx][ny] = visited[x][y] + 1 if maze[nx][ny] == 1 else visited[x][y]
                q.append((nx, ny, visited[nx][ny]))  
                print(x, "=>", nx, "/", y, "=>", ny, "appended/", visited[nx][ny])  

print(answer)
