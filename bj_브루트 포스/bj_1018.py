# 백준 브루트 포스_4 : 체스판 다시 칠하기
import sys
[N, M] = list(map(int, sys.stdin.readline().split()))

whole = []
for n in range(N) :
    whole.append(list(sys.stdin.readline().rstrip()))

startWithWhite = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                  ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                  ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
                  ]
startWithBlack = [['B', 'W', 'B', 'W', 'B', 'W','B','W'],
                  ['W', 'B', 'W', 'B', 'W', 'B','W','B'],
                  ['B', 'W', 'B', 'W', 'B', 'W','B','W'],
                  ['W', 'B', 'W', 'B', 'W', 'B','W','B'],
                  ['B', 'W', 'B', 'W', 'B', 'W','B','W'],
                  ['W', 'B', 'W', 'B', 'W', 'B','W','B'],
                  ['B', 'W', 'B', 'W', 'B', 'W','B','W'],
                  ['W', 'B', 'W', 'B', 'W', 'B','W','B']]

result1 = 64
temp = 0
for r in range(N-8+1) :
    for c in range(M-8+1) :
        for r2 in range(8) :
            for c2 in range(8) :
                if whole[r+r2][c+c2] != startWithWhite[r2][c2] :
                    temp += 1
        if temp <= result1 :
            result1 = temp
        temp = 0
    temp = 0

result2 = 64
temp = 0
for r in range(N-8+1) :
    for c in range(M-8+1) :
        for r2 in range(8) :
            for c2 in range(8) :
                if whole[r+r2][c+c2] != startWithBlack[r2][c2] :
                    temp += 1
        if temp <= result2 :
            result2 = temp
        temp = 0
    temp = 0
print(min(result1, result2))