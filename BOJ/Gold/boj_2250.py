# [백준] 트리, DFS > 트리의 높이와 너비

import sys
input = sys.stdin.readline
n = int(input())

graph = dict()
parents = [0 for _ in range(n+1)]
for _ in range(n) :
    parent, left, right = map(int, input().split())
    if left != -1 : parents[left] = parent
    if right != -1 : parents[right] = parent
    graph[parent] = [left, right]
root = parents.index(0, 1)

arr = []

def dfs(v, level) :
    graph[v].append(level)
    if graph[v][0] != -1 :
        dfs(graph[v][0], level+1)
        arr.append(v)
    
    else :
        arr.append(v)
    if graph[v][1] != -1 :
        dfs(graph[v][1], level+1)
        return
    else :
        return
    
dfs(root, 1)


depthBreath = dict()
for i in range(n) :
    left, right, level = graph[arr[i]]
    if level in depthBreath :
        if len(depthBreath[level]) == 2 :
            depthBreath[level][1] = i
        else : depthBreath[level].append(i)
    else : depthBreath[level] = [i]

level = 1
answer = 0
for i in range(2, len(depthBreath)+1) :
    if len(depthBreath[i]) == 2 and abs(depthBreath[i][1] - depthBreath[i][0]) > answer :
        answer = abs(depthBreath[i][1] - depthBreath[i][0])
        level = i

print(level, answer+1)