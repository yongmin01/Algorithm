# 백준 스택, 큐, 덱_10 : 풍선 터뜨리기

import sys
from collections import deque
N = int(sys.stdin.readline().strip())

t = list(map(int, sys.stdin.readline().split()))
d= deque()
for i in range(N) :
    d.append({i: t[i]})
print("here", d[0][0])
temp = int(d[0][0])
while len(d) != 1 :
    if temp > 0 :
        print(d.popleft())
        d.rotate(-temp)
    else :
        print(d.popleft())
        d.rotate(temp)
    print(d)
print(d[0])