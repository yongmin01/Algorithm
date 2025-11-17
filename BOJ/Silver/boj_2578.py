# [백준] 시뮬레이션 > 빙고

import sys
input = sys.stdin.readline
from collections import defaultdict

board = defaultdict(list)
for r in range(5) :
    row = list(map(int, input().split(" ")))
    for c in range(5) :
        board[row[c]].append(r)
        board[row[c]].append(c+5)
        if r == c :
            board[row[c]].append(10)
        if r + (c+5) == 9 :
            board[row[c]].append(11)

count = defaultdict(int)
bingo = 0
answer = 0
for i in range(5) :
    temp = list(map(int, input().split(' ')))
    for l in range(5) :
        for n in board[temp[l]] :
            count[n] += 1
            if count[n] == 5 : bingo += 1
            if bingo == 3 and answer == 0 : answer = (i*5) + (l+1)
            
print(answer)