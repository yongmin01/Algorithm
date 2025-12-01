# [백준] 그리디 > 회의실 배정

import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for _ in range(n) :
    start, end = map(int, input().split())
    heapq.heappush(arr, (end, start))

answer = 1
prevEnd, prevStart = heapq.heappop(arr)
while arr :
    end, start = heapq.heappop(arr)
    if prevEnd <= start :
        answer += 1
        prevEnd = end
        
print(answer)