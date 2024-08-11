# 백준_너비 우선 탐색 & 깊이 우선 탐색 : 유기농 배추

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y, temp) :
    global result
    
    if [x, y] in c :
        c.remove([x,y])
        temp.append([x,y])

        dfs(x+1, y, temp)
        dfs(x, y+1, temp)
        dfs(x-1, y, temp)
        dfs(x, y-1, temp)

        temp.pop()
        if len(temp) == 0 : 
            result += 1
        return
    else : 
        return
    
T = int(input())

for i in range(T) :
    [M, N, K] = map(int, input().split())
    c = []

    for i in range(K) :
        c.append(list(map(int, input().split())))

    result = 0

    while len(c) > 0 :
            dfs(c[0][0], c[0][1], [])

    print(result)

