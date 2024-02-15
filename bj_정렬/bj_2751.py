# 백준 정렬_4 : 수 정렬하기 2
import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N) :
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in nums :
    print(i)