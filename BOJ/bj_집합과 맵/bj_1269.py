# 백준 집합과 맵_7 : 대칭 차집합
import sys
[N, M ] = list(map(int, sys.stdin.readline().split()))


A = set(sys.stdin.readline().split())
B = set(sys.stdin.readline().split())

C = A - B | B - A
print(len(C))