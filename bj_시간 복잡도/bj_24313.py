# 백준 시간 복잡도_7 : 알고리즘 수업 - 점근적 표기 1
[a1, a2] = [int(x) for x in input().split()]
c = int(input())
n0 = int(input())

if a1*n0 + a2 <= c*n0 and c >= a1 : print(1)
else: print(0)
