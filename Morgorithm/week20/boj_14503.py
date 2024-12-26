# 백준_구현 : 로봇 청소기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

# 반시계 방향 순서로 초기 방향 변환
if d == 1 : d = 3
elif d == 3 : d = 1

graph = []
for i in range(N) :
    graph.append(list(map(int, input().split())))

# 반시계 방향으로 끊기지 않고 회전시킬 수 있도록 회전 방향 만들어두기
direction = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 0], [0, 1]]
answer = 0

while True :
    if graph[r][c] == 0 :
        answer += 1
        graph[r][c] = 2
         
    for i in range(4) :
        d += 1
        if graph[r + direction[d][0]][c + direction[d][1]] == 0 :
            r += direction[d][0]
            c += direction[d][1]
            break
        if d > 3 : d -= 4 # 회전하다가 끊기지 않도록 방향 변수 조정
        
    else :
        if d == 0 : r += 1
        elif d == 1 : c += 1
        elif d == 2 : r -= 1
        elif d == 3 : c -= 1
        if graph[r][c] == 1 : break

print(answer)