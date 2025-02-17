# 백준_백트래킹 : 도영이가 만든 맛있는 음식
# 비트마스킹 사용해서 풀어볼 것!!!

import sys
from math import inf
input = sys.stdin.readline

N = int(input())
ingredients = []

for i in range(N) :
    S, B = map(int, input().split())
    ingredients.append([S, B])

visited = [0 for _ in range(N)]

def solution(index) :
    if index == N :
        global answer
        cnt, s, b = 0, 1, 0
        for i in range(N) :
            if visited[i] :
                cnt += 1
                s *= ingredients[i][0]
                b += ingredients[i][1]
        if cnt == 0 : return
        if abs(s-b) < answer :
            answer = abs(s-b)
        return
    
    visited[index] = 1
    solution(index+1)
    visited[index] = 0
    solution(index+1)
    
   
answer = inf
solution(0)

print(answer)

