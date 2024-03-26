# 백준 심화 2_1 : 약수

import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
print(nums[0]*nums[-1])