# [백준] BFS > 상범 빌딩

import sys
input = sys.stdin.readline
from collections import deque

answers = []
while True :
    l, r, c = map(int, input().split())
    if l == r == c == 0 : break
    building = [[] for _ in range(l)]
    start, end = 0, 0
    for lIndex in range(l) :
        for rIndex in range(r) :
            col = list(input().strip())
            for cIndex in range(c) :
                if col[cIndex] == 'S' : start = [lIndex, rIndex, cIndex, 0]
                if col[cIndex] == 'E' : end = [lIndex, rIndex, cIndex]
            building[lIndex].append(col)
        input()
    q = deque()
    q.append(start)
    # 동,서,남,북,상,하 방향으로 순회
    dz = [0, 0, 0, 0, 1, -1]
    dx = [0, 0, 1, -1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    INF = int(2e9)
    answer = INF
    while q :
        layer, row, column, duration = q.popleft()
        if layer == end[0] and row == end[1] and column == end[2] : 
            answer = duration
            break
        for i in range(6) :
            nz = layer + dz[i]
            nx = row + dx[i]
            ny = column + dy[i]
            if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l and (building[nz][nx][ny] == '.' or building[nz][nx][ny] == 'E'):
                building[nz][nx][ny] = duration + 1
                q.append([nz, nx, ny, duration+1])
    
    if answer != INF :  answers.append(f"Escaped in {answer} minute(s).")
    else : answers.append("Trapped!")

for i in answers :
    print(i)