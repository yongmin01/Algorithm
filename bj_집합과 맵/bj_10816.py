# 백준 집합과 맵_5 : 숫자 카드 2
import sys
N = int(sys.stdin.readline().rstrip())
has = {}
temp = list(map(int, sys.stdin.readline().split()))
for i in temp :
    if i in has :
        has[i] += 1
    else : has[i] = 1

M = int(sys.stdin.readline().rstrip())
quiz = list(map(int, sys.stdin.readline().split()))
for i in quiz :
    if i in has :
        print(has[i], end=" ")
    else :
        print(0, end=" ")