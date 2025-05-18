# [백준] 그래프 이론 : 적록색약

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
graph = []
for r in range(N) :
    graph.append(list(map(str, input().rstrip())))

def dfs(graph, visited, x, y, color) :
    if x < 0 or x >= N or y < 0 or y >= N or graph[x][y] != color:
        return False
    if visited[x][y] == False :
        visited[x][y] = True
        if color == 'G' : graph[x][y] = 'R'
        dfs(graph, visited, x-1, y, color)
        dfs(graph, visited, x, y+1, color)
        dfs(graph, visited, x+1, y, color)
        dfs(graph, visited, x, y-1, color)
        return True
    return False

visited = [[False for _ in range(N)] for _ in range(N)]
notblindness = 0
for r in range(N) :
    for c in range(N) :
        if dfs(graph, visited, r, c, graph[r][c]) :
            notblindness += 1


visited = [[False for _ in range(N)] for _ in range(N)]
blindness = 0
for r in range(N) :
    for c in range(N) :
        if dfs(graph, visited, r, c, graph[r][c]) :
            blindness += 1
print(notblindness, blindness)