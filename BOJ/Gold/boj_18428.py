# [백준] 브루트포스, 백트래킹 > 감시 피하기

import sys 
input = sys.stdin.readline
from itertools import combinations
from collections import deque

n = int(input())
graph = []
x_pos = [] # 장애물을 놓을 수 있는 빈 칸 수집
for r in range(n) :
    row = list(input().split())
    for c in range(n) :
        if row[c] != 'S' and row[c] != 'T' : 
             x_pos.append((r, c))
    graph.append(row)

def backtraking() :
    # 행 방향 검사
    for r in range(n) :
        q = deque()
        for c in range(n) :
            if graph[r][c] == 'S' :
                if q and q[-1] == 'T' : return False
                else : q.append(graph[r][c])
            elif graph[r][c] == 'T' :
                if q and q[-1] == 'S' : return False
                else : q.append(graph[r][c])
            elif graph[r][c] == 'O' : q.append(graph[r][c])
        
    q = deque()

    # 열 방향 검사
    for c in range(n) :
        q = deque()
        for r in range(n) :
            if graph[r][c] == 'S' :
                if q and q[-1] == 'T' : return False
                else : q.append(graph[r][c])
            elif graph[r][c] == 'T' :
                if q and q[-1] == 'S' : return False
                else : q.append(graph[r][c])
            elif graph[r][c] == 'O' : q.append(graph[r][c])
    return True

# 장애물을 놓을 수 있는 모든 좌표들 중에 3개를 골라(조합) 배치하고 검사
for per in combinations(x_pos, 3) :
    for p in per : # 장애물 배치
        graph[p[0]][p[1]] = 'O'

    if backtraking() :
        print("YES")
        exit()
    else : # 해당 조합으로 배치했을 때 학생들이 감시를 피할 수 없다면 그래프 원상복귀
        for p in per :
            graph[p[0]][p[1]] = 'X'
print("NO")
