# [백준] 그리디 > 로프

import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N) :
    ropes.append(int(input()))

ropes.sort(reverse=True)

answer = ropes[0]
for i in range(N) :
    if ropes[i] * (i+1) >= answer :
        answer = ropes[i] * (i+1)
    
print(answer)