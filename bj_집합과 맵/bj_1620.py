# 집합과 맵_4 : 나는야 포켓몬 마스터 이다솜
import sys
[N, M] = list(map(int, sys.stdin.readline().rstrip().split()))
name = {}
num = {}
for i in range(N) :
    temp = sys.stdin.readline().rstrip()
    name[temp] = i+1
    num[i+1] = temp

for i in range(M) :
    q = sys.stdin.readline().rstrip()
    if q.isdecimal() :
        print(num[int(q)])
    else :
        print(name[q])

