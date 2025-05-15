# [프로그래머스] 깊이/너비 우선 탐색(DFS/BFS) : 네트워크

def dfs(v, visited, graph) :
    visited[v] = True
    for i in range(len(visited)) :
        if i != v and visited[i] == False and graph[v][i] == 1 :
            dfs(i, visited, graph)
    return
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n) :
        if visited[i] == False :
            answer += 1
            dfs(i, visited, computers)
        
    return answer

