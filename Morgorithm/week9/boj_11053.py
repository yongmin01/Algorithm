# 백준_DP : 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
DP = [1 for _ in range(N)]

for i in range(N) :
    for l in range(i+1, N) :
        if A[i] < A[l] :
            DP[l] = max(DP[i]+1, DP[l])
        
print(max(DP))