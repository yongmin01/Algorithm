# [백준] 백트래킹 > 부분수열의 합     

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

def backtracking(size, stack, start) :
    global answer
    if len(stack) == size :
        if sum(stack) == s :
            answer += 1
        return
    
    for i in range(start, n) :
        stack.append(arr[i])
        backtracking(size, stack, i+1)
        stack.pop()
    return
    


for size in range(1, n+1) :
    backtracking(size, [], 0)
print(answer)