# 백준_브루투포스 & 백트래킹 : 치킨배달

import sys
input = sys.stdin.readline
import math

N, M = list(map(int, input().split()))
village = [] # 마을
houses = [] # 집 위치
current_chicken = [] # 치킨집 위치
for i in range(N) :
    row = list(map(int, input().split()))
    for l in range(N) :
        if row[l] == 1 :
            houses.append((i, l))
        elif row[l] == 2 :
            current_chicken.append((i,l))
    village.append(row)

distance = [] # 집과 치킨집들간의 거리 집합
for house in houses :
        temp = []
        for chicken in current_chicken :
            temp.append(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        distance.append(temp)

temp = []
minimum = math.inf
def backtracking(s) :
    global minimum
    if len(temp) == M :
        total_distance = 0
        for dis in distance :
            candidate_distances = []
            for candidate in temp :
                candidate_distances.append(dis[candidate])
            total_distance += min(candidate_distances)
            if total_distance > minimum :
                temp.pop()
                return
        minimum = total_distance
        temp.pop()
        return

    for i in range(s, len(current_chicken)) :
        temp.append(i)
        backtracking(i+1)
    if len(temp) > 0 :
        temp.pop()
        return

backtracking(0)
print(minimum)