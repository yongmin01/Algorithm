#  백준 집합과 맵_6 : 듣보잡

import sys
[N, M] = list(map(int, sys.stdin.readline().split()))
notheard = set()
notseen = set()
for i in range(N) :
    notheard.add(sys.stdin.readline().rstrip())
for i in range(M) :
    notseen.add(sys.stdin.readline().rstrip())
result = notheard & notseen
print(len(result))
r = sorted(list(result))
for i in r :
    print(i)