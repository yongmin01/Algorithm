# [백준] DP > 가장 큰 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n) :
    temp = 0
    for k in range(i-1, -1, -1) :
        if arr[i] > arr[k] :
            if dp[k] > temp :
                temp = dp[k]
        if k == 0 :
            dp[i] = temp + arr[i]
            
print(max(dp))


### 1차 시도 ###
# 반례
# 8
# 3  10  2  7  11  5  13  8
# 자기보다 작은 수가 나올 때까지 stack에서 다 pop 해버려서 앞쪽의 큰 수가 쌓이지 못함(작은 수를 pass하지 못함)

# import sys
# input = sys.stdin.readline
# from collections import deque

# n = int(input())
# arr = list(map(int, input().split()))

# stack = deque()
# answer = [0 for _ in range(n)]
# for i in range(n) :
#     if stack :
#         if stack[-1] < arr[i] :
#             stack.append(arr[i])
#             answer[i] = answer[i-1] + arr[i]
#         else :
#             answer[i] = answer[i-1] + arr[i]
#             k = i
#             while stack[-1] >= arr[i] :
#                 answer[i] -= stack.pop()
#                 k -= 1
#                 if len(stack) == 0 : 
#                     break
#             stack.append(arr[i])
#     else :
#         stack.append(arr[i])
#         answer[i] = arr[i]

# print(max(answer))


# 2차 시도
# 반례
# 8
# 7 8 9 2 6 7 8 10

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# dp = [0 for _ in range(n)]

# top = arr[0]
# dp[0] = arr[0]
# answer = 0

# for start in range(1, n) :
#     dp = [0 for _ in range(n)]
#     dp[start-1] = arr[start-1]
    
#     for i in range(start, n) :
#         if arr[i] > top :
#             top = arr[i]
#             dp[i] = dp[i-1] + arr[i]
#         else :
#             dp[i] = dp[i-1]
#     if dp[-1] > answer : answer = dp[-1]
#     top = arr[start]

# print(answer)