# 백준 정렬_7 : 좌표 정렬하기
import sys

N = int(sys.stdin.readline())
cor =[]
for i in range(N) :
    [x, y] = list(map(int, sys.stdin.readline().split()))
    cor.append([x, y])
cor.sort(key=lambda x: (x[0], x[1]))
for i in cor :
    print(i[0], i[1])