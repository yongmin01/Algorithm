# [백준] 브루트포스 + BFS > 연구소

import sys
input = sys.stdin.readline
from itertools import combinations
import copy
from collections import deque

n, m = map(int, input().split())
maps = []
empty = []
virus = []
wall = 0

for r in range(n) :
    row = list(map(int, input().split()))
    for c in range(m) :
        if row[c] == 0 :
            empty.append([r, c])
        elif row[c] == 1 :
            wall += 1
        else : 
            virus.append([r, c])
    maps.append(row)

combs = combinations(empty, 3)
answer = n*m
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for comb in combs :
    visited = copy.deepcopy(maps)
    infected = 0
    for x, y in comb :
        visited[x][y] = 1

    for v in virus :
        q = deque()
        q.append(v)
    
        while q :
            x, y = q.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
                    infected += 1
                    visited[nx][ny] = -1
                    q.append([nx, ny])
                    
    answer = min(answer, infected)

print(n*m-len(virus)-wall-3-answer)