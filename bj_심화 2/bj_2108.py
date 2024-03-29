# 백준 심화 2_4 : 통계학

import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N) :
    nums.append(int(sys.stdin.readline().rstrip()))
sortedNums = sorted(nums)
snums = {}
for i in sorted(set(nums)) :
    snums[i] = 0

# 산술 평균
print(round(sum(nums) / N))

# 중앙값
print(sortedNums[int(N/2)])

# 최빈값
for i in nums :
    snums[i] += 1
m = [k for k, v in snums.items() if max(snums.values()) == v]
if len(m) > 1 :
    print(m[1])
else : print(m[0])

# 범위
print(sortedNums[-1] - sortedNums[0])