# [백준] 백트래킹 > 게란으로 계란치기

import sys
input = sys.stdin.readline

n = int(input())
eggs = []
for _ in range(n) :
    eggs.append(list(map(int, input().split())))

answer = 0
def backtracking(curr) :
    global answer
    if curr == n :
        temp = 0
        for egg in eggs :
            if egg[0] <= 0 :
                temp += 1
        answer = max(answer, temp)
        return
    if eggs[curr][0] <= 0 : # 현재 계란이 깨졌으면 바로 다음 계란으로 넘어가기
        backtracking(curr+1)
    else :
        for k in range(n) :
            if curr != k and eggs[k][0] > 0 : # 현재 계란이 안 깨졌고, i번째 계란도 안 깨졌으면 깬다!
                eggs[curr][0] -= eggs[k][1]
                eggs[k][0] -= eggs[curr][1]
                backtracking(curr+1) # 다음 계란으로 깰 수 있는 계란 찾기
                eggs[curr][0] += eggs[k][1]
                eggs[k][0] += eggs[curr][1] # 현재 계란과 i 번째 계란 원상복구
        else :
            backtracking(n)
            
backtracking(0)

print(answer)
