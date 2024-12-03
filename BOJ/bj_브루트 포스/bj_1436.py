# 백준 브루트 포스 5 : 영화감독 숌
import sys
N = int(sys.stdin.readline())

num = 665
nums = []
while len(nums) < N :
    num += 1
    if ("666" in str(num)) :
        nums.append(str(num))
print(nums[-1])