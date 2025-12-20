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

#######

import sys
input = sys.stdin.readline

arr= []
pos = []
for r in range(5) :
    row = list(input().strip())
    for c in range(5) :
        pos.append([r, c])
    arr.append(row)

pos_len = len(pos)

combs = []
def make_comb(s, li, count) :
    global combs
    if len(li) == 7 and count >= 4 :
        combs.append(li)
        return
    for i in range(s, pos_len) :
        r, c = pos[i]
        if 7 - len(li) <= 4 - count :
            if arr[r][c] == 'S' :
                li.append([r, c])
                make_comb(i+1, li, count+1)
                count -= 1
                li.pop()
        else :
            if arr[r][c] == 'S' :
                li.append([r, c])
                make_comb(i+1, li, count+1)
                count -= 1
                li.pop()
            else : 
                li.append([r, c])
                make_comb(i+1, li, count)
                li.pop()
make_comb(0, [], 0)
print(len(combs))
