# [백준] DFS > Two Dots

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n) :
    board.append(input().strip())

def dfs(x, y, prevColor, prevDis) :
    if not (0 <= x < n and 0 <= y < m and board[x][y] == prevColor) :
        return False
    if visited[x][y] == 1 and prevDis >= 4 :
        print("Yes")
        exit()
    if visited[x][y] == 0 :
        visited[x][y] = prevDis + 1
        dfs(x+1, y, board[x][y], visited[x][y])
        dfs(x, y-1, board[x][y], visited[x][y])
        dfs(x-1, y, board[x][y], visited[x][y])
        dfs(x, y+1, board[x][y], visited[x][y])
        visited[x][y] = 0
        return False


# 시작 가능 지점 찾기
for r in range(n-1) :
    for c in range(m-1) :
        curColor = board[r][c]
        if board[r+1][c] == curColor and board[r][c+1] == curColor :
            dfs(r, c, board[r][c], 0)
print("No")