# [백준] 구현 > 톱니바퀴

from collections import deque

# 자신이 회전할 때 어떤 톱니를 함께 확인해야하는지 기록해둔 것
wheelspos = [[], [2], [1, 3], [2, 4], [3]]

# a바퀴와 b바퀴를 돌릴 때 각각 자신의 몇번째 톱니를 확인해야하는지 기록해둔 것
# ex) a=2, b=3 =-> 2번 바퀴의 (toothset[2][3]=)2번 톱니와 3번 바퀴의 (toothset[3][2]=)6번 톱니가 같은 극인지 확인
toothset = [[], 
            [-1, -1, 2, -1, -1], 
            [-1, 6, -1, 2, -1],
            [-1, -1, 6, -1, 2],
            [-1, -1, -1, 6, -1]
            ]

def rotate(i, d) :
    for t in wheelspos[i] :
        if not rotated[t] :
            if wheels[i][toothset[i][t]] != wheels[t][toothset[t][i]] :
                rotated[t] = True
                orders.append([t, -d])
                rotate(t, -d)

wheels = [[]]
for _ in range(4) :
    wheels.append(deque(input().strip()))        

k = int(input())
for _ in range(k) :
    wheel, direction = map(int, input().split())
    
    orders = []
    orders.append([wheel, direction])
    rotated = [False for _ in range(5)]
    rotated[wheel] = True

    # 회전할 바퀴를 연쇄적으로 확인
    rotate(wheel, direction)

    # 실제 회전(톱니 업데이트)
    for i, d in orders :
        if d == 1 : # 시계 방향으로 회전
            wheels[i].appendleft(wheels[i].pop())
        else : # 반시계 방향으로 회전
            wheels[i].append(wheels[i].popleft())

    orders = []
    rotated = [False for _ in range(5)]

answer = 0
for i in range(1, 5) :
    if wheels[i][0] == '1' :
        answer += pow(2, i-1)
print(answer)
