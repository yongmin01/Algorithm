# 백준_스택 : 오큰수

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [-1]
stack = [arr[-1]]
for i in range(N-2, -1, -1) :
    while stack[-1] <= arr[i] :
        stack.pop()
        if len(stack) == 0 : break
    if len(stack) == 0 :
        result.append(-1)
        stack.append(arr[i])
    else :
        result.append(stack[-1])
        stack.append(arr[i])
    
for i in reversed(result) :
    print(i, end=" ")
