# 백준 정렬_11 : 좌표 압축
import sys
N = int(sys.stdin.readline())
nums = [int(x) for x in sys.stdin.readline().split()]

nums_sorted = sorted(set(nums))
dic = {}
for i in range(len(nums_sorted)) :
    dic[nums_sorted[i]] = i

for i in nums :
    print(dic[i], end=" ")