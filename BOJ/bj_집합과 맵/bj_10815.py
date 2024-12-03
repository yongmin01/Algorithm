# 백준 집합과 맵_1 : 숫자 카드

import sys
card = [0 for x in range(20000001)]
N = int(sys.stdin.readline())

has = list(map(int, sys.stdin.readline().split()))
for i in range(N) :
    card[has[i]] = 1

M = int(sys.stdin.readline())
ask = list(map(int, sys.stdin.readline().split()))
for i in ask :
    if card[i] == 1 :
        print(1, end=" ")
    else : print(0, end=" ")
