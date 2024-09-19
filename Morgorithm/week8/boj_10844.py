# 백준_DP : 쉬운 계단 수

import sys
input = sys.stdin.readline

N = int(input())
nums = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for n in range(N)]
for i in range(1, 10) :
    nums[0][i] = 1

for i in range(1, N) :
    for l in range(10) :
        if l == 0 :
            nums[i][l] = nums[i-1][l+1]
        elif l == 9 :
            nums[i][l] = nums[i-1][l-1]
        else :
            nums[i][l] = nums[i-1][l-1] + nums[i-1][l+1]
print(sum(nums[N-1]) % 1000000000)