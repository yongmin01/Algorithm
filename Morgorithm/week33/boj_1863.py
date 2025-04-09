# 백준_스택 : 스카이라인 쉬운거

import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = 0
for i in range(n) :
    x, y = list(map(int, input().split()))
    if (len(stack) == 0 or y > stack[-1]) and y != 0 :
        stack.append(y)
    else :
        while len(stack) > 0 and stack[-1] > y :
            stack.pop()
            answer += 1
        if len(stack) == 0 and y != 0 :
            stack.append(y)
        elif len(stack) > 0 and stack[-1] < y :
            stack.append(y)
print(answer + len(stack))