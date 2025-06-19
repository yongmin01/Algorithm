# [백준] 브루트포스 > 부분수열의 합

import sys
input = sys.stdin.readline
from itertools import combinations

n, s = map(int, input().split())

arr = list(map(int, input().strip().split()))

answer = 0
for i in range(1, n+1) :
    comb = list(combinations(arr, i))
    for c in comb :
        if sum(c) == s :
            answer += 1
print(answer)


# 백트래킹 풀이

# import sys
# input = sys.stdin.readline

# n, s = map(int, input().split())
# arr = list(map(int, input().split()))

# answer = 0

# def backtracking(size, stack, start) :
#     global answer
#     if len(stack) == size :
#         if sum(stack) == s :
#             answer += 1
#         return
    
#     for i in range(start, n) :
#         stack.append(arr[i])
#         backtracking(size, stack, i+1)
#         stack.pop()
#     return
    


# for size in range(1, n+1) :
#     backtracking(size, [], 0)
# print(answer)