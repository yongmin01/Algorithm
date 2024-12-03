# 백준 정렬_8 : 좌표 정렬하기 2
import sys

N = int(sys.stdin.readline())
cor =[]
for i in range(N) :
    [x, y] = list(map(int, sys.stdin.readline().split()))
    cor.append([x, y])
cor.sort(key=lambda x: (x[1], x[0]))
for i in cor :
    print(i[0], i[1])