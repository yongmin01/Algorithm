# 집합과 맵_4 : 나는야 포켓몬 마스터 이다솜
import sys
[N, M] = list(map(int, sys.stdin.readline().rstrip().split()))
has = []
for i in range(N) :
    has.append(sys.stdin.readline().rstrip())
print(has)
for i in range(M) :
    q = sys.stdin.readline().rstrip()
    if q.isdecimal() :
        print(has[int(q)-1])
    else :
        print(has.index(q) + 1)