# [백준] 구현, 브루트포스 > 테트로미노

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
def dfs(r, c, collect, sum) :
    global answer

    if collect == 4 :
        if answer < sum :
            answer = sum
        return
    else :
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4) :
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                dfs(nx, ny, collect+1, sum+graph[nx][ny])
                visited[nx][ny] = 0
        return
for r in range(n) :
    for c in range(m) :
        visited[r][c] = 1
        dfs(r, c, 1, graph[r][c])
        visited[r][c] = 0
        # ㅜ 모양 테트로미노는 DFS를 통해 만들어질 수 없으므로 따로 고려
        if c >= 1 and c <= m-2 and r >= 1 :# ㅗ 모양
            temp = graph[r][c] + graph[r][c-1] + graph[r][c+1] + graph[r-1][c]
            if answer < temp : answer = temp
        if c >= 1 and c <= m-2 and r <= n-2 : # ㅜ 모양
            temp = graph[r][c] + graph[r][c-1] + graph[r][c+1] + graph[r+1][c]
            if answer < temp : answer = temp
        if r >= 1 and r <= n-2 and c >= 1 : # ㅓ 모양
            temp = graph[r][c] + graph[r-1][c] + graph[r+1][c] + graph[r][c-1]
            if answer < temp : answer = temp
        if r >= 1 and r <= n-2 and c <= m-2 : # ㅏ 모양
            temp = graph[r][c] + graph[r-1][c] + graph[r+1][c] + graph[r][c+1]
            if answer < temp : answer = temp

print(answer)
