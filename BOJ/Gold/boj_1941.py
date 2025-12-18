# [백준] 브루트포스 > 소문난 칠공주

import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

arr = []
for _ in range(5) :
    arr.append(list(input().strip()))

pos = []
for r in range(5) :
    for c in range(5) :
        pos.append([r, c])
combs = combinations(pos, 7)
candidates = []
for comb in combs :
    count = 0
    for x, y in comb :
        if arr[x][y] == 'S' : count += 1
    if count >= 4 : 
        candidates.append(list(comb))
print(len(candidates))
def bfs() :
    global q
    while q :
        x, y = q.popleft()
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 :
                if (nx, ny) in visited and visited[(nx, ny)] == False :
                    visited[(nx, ny)] = True
                    q.append([nx, ny])
answer = 0
for candidate in candidates :
    visited = dict()
    q = deque()
    for c in candidate :
        visited[tuple(c)] = False
    visited[tuple(candidate[0])] = True
    q.append(candidate[0])
    bfs()
    for v in visited.values() :
        if not v : break
    else : answer += 1
print(answer)
