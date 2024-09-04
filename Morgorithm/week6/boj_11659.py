# 백준_누적 합 : 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
sums = [0]

for i in range(1, N+1) :
    sums.append(sums[i-1] + nums[i-1])

for _ in range(M) :
    i, j = list(map(int, input().split()))
    if i == j : print(nums[i-1])
    else :
        print(sums[j] - sums[i-1])
