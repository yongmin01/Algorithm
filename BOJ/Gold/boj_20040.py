# [백준] 분리 집합 > 사이클 게임

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

parents = [i for i in range(n)]

def find_parents(x) :
    if parents[x] != x :
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(v1, v2) :
    p1 = find_parents(v1)
    p2 = find_parents(v2)
    if p1 < p2 :
        parents[p2] = p1 # 부모끼리 합쳐야 집합 전체가 합쳐짐
    else :
        parents[p1] = p2

answer = 0
for i in range(1, m+1) :
    v1, v2 = map(int, input().split())
    if find_parents(v1) == find_parents(v2) :
        if answer == 0 : 
            answer = i
    else :
        union(v1, v2)

print(answer)