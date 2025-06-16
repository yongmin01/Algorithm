# [백준] 브루트포스 > 부분수열의 합

import sys
input = sys.stdin.readline
from itertools import combinations

n, s = map(int, input().split())

arr = list(map(int, input().strip().split()))

answer = 0
for i in range(1, n+1) :
    comb = list(combinations(arr, i))
    for c in comb :
        if sum(c) == s :
            answer += 1
print(answer)