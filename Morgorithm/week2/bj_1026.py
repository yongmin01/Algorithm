# 백준_정렬 & 그리디 알고리즘 : 보물

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

result = 0
for i in range(N) :
    result += A[i] * B[i]
    
print(result)
