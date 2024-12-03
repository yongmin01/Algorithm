# 백준 스택, 큐, 덱_10 : 풍선 터뜨리기

import sys
from collections import deque
N = int(sys.stdin.readline().strip())

t = list(map(int, sys.stdin.readline().split()))
d = deque()
for i in range(N) :
    d.append((i,t[i]))
while len(d) != 1 :
    if d[0][1] > 0 :
        temp = d[0][1]
        print(d[0][0]+1, end=" ")
        d.popleft()
        for i in range(0, temp-1) : 
            d.append(d[0])
            d.popleft()
    else :
        temp = d[0][1]
        print(d[0][0]+1, end=" ")
        d.popleft()
        for i in range(0, -temp) : 
            d.appendleft(d[-1])
            d.pop()
print(d[0][0]+1)