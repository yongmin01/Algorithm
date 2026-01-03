# [백준] 구현 > 빗물

import sys
input = sys.stdin.readline
from collections import deque

h, w = map(int, input().split())
pillars = list(map(int, input().split()))
stack = deque()
answer = 0

for r in range(1, h+1) :
    count = 0
    for c in range(w) :
        if pillars[c] >= r : # 현재 칸이 기둥이라는 뜻
            if stack :
                answer += count
                stack.popleft()
                stack.append(c)
                count = 0
            else : 
                stack.append(c)
        else : # 현재 칸이 비었다는 뜻
            if stack :
                count += 1
    stack = deque()
    
print(answer)
