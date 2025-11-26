# [백준] 투 포인터 > 수 고르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = []
for _ in range(n) :
    nums.append(int(input()))
nums.sort()

left, right = 0, 1
answer = 2 * pow(10, 9)
while right < n :
    if nums[right] - nums[left] == m : 
        print(m)
        exit()

    if nums[right] - nums[left] < m :
        right += 1
    else :
        answer = min(answer, nums[right] - nums[left])
        left += 1

print(answer)
