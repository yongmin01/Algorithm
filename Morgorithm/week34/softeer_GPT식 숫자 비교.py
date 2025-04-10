# Softeer : GPT식 숫자 비교

import sys
input = sys.stdin.readline

N = int(input())
nums = [False for _ in range(100102)]
nums_count = [0 for _ in range(100102)]
for i in range(N) :
    num = input().rstrip().split('.')
    if len(num) == 1 :
        nums[int(num[0]) * 1001] = num[0]
        nums_count[int(num[0]) * 1001] += 1
    else :
        nums[int(num[0]) * 1001 + int(num[1]) + 1] = '.'.join(num)
        nums_count[int(num[0]) * 1001 + int(num[1]) + 1] += 1
        
for i in range(len(nums)) :
    if nums[i] :
        for l in range(nums_count[i]) :
                print(nums[i])