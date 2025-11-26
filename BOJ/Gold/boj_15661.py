# [백준] 백트래킹 > 링크와 스타트

import sys
input = sys.stdin.readline

N = int(input())
skills = []
for _ in range(N) :
    skills.append(list(map(int, input().split())))

answer = int(1e9)

visited = [False] * N

def getSkillSet() :
    global answer
    start, link = 0, 0
    for i in range(N) :
        for j in range(N) :
            if visited[i] and visited[j] : start += skills[i][j]
            elif not visited[i] and not visited[j] : link += skills[i][j]
    answer = min(answer, abs(start - link))
    return

def backtracking(i) :
    if i == N :
        getSkillSet()
        return
    visited[i] = True
    backtracking(i+1)
    visited[i] = False
    backtracking(i+1)

backtracking(0)
print(answer)
