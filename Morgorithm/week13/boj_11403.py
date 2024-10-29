# 백준_Floyd-Warshall : 경로 찾기

import sys
input = sys.stdin.readline
from math import inf

N = int(input())
graph = []

for i in range(N) :
    graph.append(list(map(int, input().split())))

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 0 :
            graph[i][j] = inf

for m in range(N) :
    for i in range(N) :
        for j in range(N) :
                    graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == inf :
            print(0, end= " ")
        else : print(1, end=" ")
    print()