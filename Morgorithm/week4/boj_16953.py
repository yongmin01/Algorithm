# 백준_너비 우선 탐색 : A -> B

import sys
input = sys.stdin.readline
from collections import deque

[A, B] = map(int, input().split())

queue = deque()
queue.append((A,0))

while queue :
    curr = queue.popleft()
    if curr[0] == B :
        print(curr[1]+1)
        exit()
    elif curr[0] > B :
        continue
    else :
        queue.append((curr[0]*2, curr[1]+1))
        queue.append((curr[0]*10+1, curr[1]+1))

print(-1)
