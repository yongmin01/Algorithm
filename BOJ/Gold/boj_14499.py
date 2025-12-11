# [백준] 구현 > 주사위 굴리기

import sys
input = sys.stdin.readline

# 현재   상 동  남 서 북  하
dice = [0, 0, 0, 0, 0, 0]
# 상 0
# 동 1
# 남 2
# 서 3
# 북 4
# 하 5

# 동쪽으로 굴리면 (1)
# 0 -> 1
# 1 -> 5
# 2 -> x
# 3 -> 0
# 4 -> x
# 5 -> 3
def east() :
    global dice
    temp = dice[:]
    dice[1] = temp[0]
    dice[5] = temp[1]
    dice[0] = temp[3]
    dice[3] = temp[5]
    return [dice[0], dice[5]]

# 서쪽으로 굴리면 (2)
# 0 -> 3
# 1 -> 0
# 2 -> x
# 3 -> 5
# 4 -> x
# 5 -> 1
def west() :
    global dice
    temp = dice[:]
    dice[3] = temp[0]
    dice[0] = temp[1]
    dice[5] = temp[3]
    dice[1] = temp[5]
    return [dice[0], dice[5]]

# 북쪽으로 굴리면(3)
# 0 -> 4
# 1 -> x
# 2 -> 0
# 3 -> x
# 4 -> 5
# 5 -> 2
def north() :
    global dice
    temp = dice[:]
    dice[4] = temp[0]
    dice[0] = temp[2]
    dice[5] = temp[4]
    dice[2] = temp[5]
    return [dice[0], dice[5]]

# 남쪽으로 굴리면(4)
# 0 -> 2
# 1 -> x
# 2 -> 5
# 3 -> x
# 4 -> 0
# 5 -> 4
def south() :
    global dice
    temp = dice[:]
    dice[2] = temp[0]
    dice[5] = temp[2]
    dice[0] = temp[4]
    dice[4] = temp[5]
    return [dice[0], dice[5]]

n, m, x, y, k = map(int, input().split())

maps =[]
for r in range(n) :
    row = list(map(int, input().split()))
    maps.append(row)


orders = list(map(int, input().split()))

for order in orders :
    if order == 1 : # 동쪽
        y += 1
        if 0 <= x < n and 0 <= y < m :
            top, down = east()
            if maps[x][y] == 0 :
                maps[x][y] = down
            else :
                dice[5] = maps[x][y]
                maps[x][y] = 0
            print(top)
        else : y -= 1
    elif order == 2 : # 서쪽
        y -= 1
        if 0 <= x < n and 0 <= y < m :
            top, down = west()
            if maps[x][y] == 0 :
                maps[x][y] = down
            else :
                dice[5] = maps[x][y]
                maps[x][y] = 0
            print(top)
        else : y += 1
    elif order == 3 : # 북쪽
        x -= 1
        if 0 <= x < n and 0 <= y < m :
            top, down = north()
            if maps[x][y] == 0 :
                maps[x][y] = down
            else :
                dice[5] = maps[x][y]
                maps[x][y] = 0
            print(top)
        else : x += 1
    else : # 남쪽
        x += 1
        if 0 <= x < n and 0 <= y < m :
            top, down = south()
            if maps[x][y] == 0 :
                maps[x][y] = down
            else :
                dice[5] = maps[x][y]
                maps[x][y] = 0
            print(top)
        else : x -= 1