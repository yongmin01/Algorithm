# [백준] 최단 경로 > 친구

import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)
graph = [[INF for _ in range(n)] for _ in range(n)]

for a in range(n) :
    friends = input().strip()
    for b in range(n) :
        if friends[b] == 'Y' : 
            graph[a][b] = 1


for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for a in range(n) :
    count = 0
    for b in range(n) :
        if graph[a][b] <= 2 :
            count += 1
    if count > answer : answer = count

if answer == 0 : 
    print(0) 
else :
    print(answer - 1)
