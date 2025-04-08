# 백준_구현 : 창고 다각형

import sys
input= sys.stdin.readline

N = int(input())
cols = []
for _ in range (N) :
    cols.append(list(map(int, input().split())))

cols.sort(key=lambda x : x[0])
height = [0 for i in range(cols[-1][0] + 1)]

max_index = 0
for col in cols :
    height[col[0]] = col[1]
    if col[1] > height[max_index] :
        max_index = col[0]

front_max = cols[0][1]
for i in range(cols[0][0] + 1, max_index) :
    if height[i] <= front_max :
        height[i] = front_max
    else :
        front_max = height[i]

rear_max = cols[-1][1]
for i in range(cols[-1][0] -1, max_index, -1) :
    if height[i] <= rear_max :
        height[i] = rear_max
    else :
        rear_max = height[i]

print(sum(height))