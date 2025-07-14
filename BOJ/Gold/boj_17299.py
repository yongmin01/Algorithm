# [백준] 자료구조, 스택 > 오등큰수

import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

count = Counter(arr)

answer = [-1 for _ in range(n)]
stack = []
for i in range(n) :
    while stack and count[arr[stack[-1]]] < count[arr[i]] :
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(' '.join(list(map(str, answer))))
