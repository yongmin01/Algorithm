# 백준_Floyd-Warshall : 플로이드

import sys
input = sys.stdin.readline
from math import inf

n = int(input())
m = int(input())
distance =[[inf for x in range(n)] for y in range(n)]

for i in range(m) :
    a, b, c = map(int, input().split())
    distance[a-1][b-1] = min(distance[a-1][b-1], c)

for m in range(n) :
    for a in range(n) :
        for b in range(n) :
            if a == b : continue
            distance[a][b] = min(distance[a][b], distance[a][m] + distance[m][b])
          

for i in range(n) :
    for j in range(n) :
        if  distance[i][j] == inf :
            print(0, end=" ")
        else : print(distance[i][j], end=" ")
    print()