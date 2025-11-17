# [백준] 브루트포스 > 사탕 게임

import sys
input = sys.stdin.readline

N = int(input())
board = []
for r in range(N) :
    board.append(list(input().strip()))

def sol(r, c, direction) :
    cc = 1
    # c 열 검사
    prev = board[0][c]
    continuecount = 1
    for i in range(1, N) :
        if board[i][c] == prev : 
            continuecount += 1
            cc = max(cc, continuecount)
        else : 
            prev = board[i][c]
            continuecount = 1

    # r 행 검사
    prev = board[r][0]
    continuecount = 1
    for i in range(1, N) :
        if board[r][i] == prev : 
            continuecount += 1
            cc = max(cc, continuecount)
        else : 
            prev = board[r][i]
            continuecount = 1
    
    if direction == "col" : # 오른쪽 칸과 교환한 경우
        # c+1 열 검사
        prev = board[0][c+1]
        continuecount = 1
        for i in range(1, N) :
            if board[i][c+1] == prev : 
                continuecount += 1
                cc = max(cc, continuecount)
            else : 
                prev = board[i][c+1]
                continuecount = 1
    else : # 아래쪽 칸과 교환한 경우
        # r+1 행 검사
        prev = board[r+1][0]
        continuecount = 1
        for i in range(1, N) :
            if board[r+1][i] == prev : 
                continuecount += 1
                cc = max(cc, continuecount)
            else : 
                prev = board[r+1][i]
                continuecount = 1
    return cc

answer = 1
for r in range(N) :
    for c in range(N) :
        if c < N-1 :
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c] # 오른쪽 칸과 교환
            answer = max(answer, sol(r, c, "col"))
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c] # 원위치
        if r < N -1 :
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c] # 아래쪽 칸과 교환
            answer = max(answer, sol(r, c, "row"))
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c] # 원위치
        
print(answer)