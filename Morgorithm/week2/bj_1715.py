# 백준_자료구조 & 그리디 알고리즘 : 카드 정렬하기

import heapq
import sys
input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N) :
    stack.append(int(input()))

heapq.heapify(stack) 
result = 0
while len(stack) != 1 :
    temp = heapq.heappop(stack) + heapq.heappop(stack)
    result += temp 
    heapq.heappush(stack, temp) 
print(result)
