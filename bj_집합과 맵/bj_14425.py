# 백준 집합과 맵_2 : 문자열 집합
import sys
[N, M] = list(map(int, sys.stdin.readline().split()))
S = []
for i in range(N) :
    S.append(sys.stdin.readline())

count = 0
for i in range(M) :
    test = sys.stdin.readline()
    if test in S :
        count += 1

print(count)