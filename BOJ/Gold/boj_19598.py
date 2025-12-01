# [백준] 그리디 > 최소 회의실 개수
 
import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for _ in range(n) :
    start, end = map(int, input().split())
    heapq.heappush(arr, (start, end))

answer = 1
start, end = heapq.heappop(arr)
ends = []
heapq.heappush(ends, end)
while arr :
    start, end = heapq.heappop(arr)
    lastEnd = heapq.heappop(ends)
    if lastEnd <= start :
        heapq.heappush(ends, end)
        
    else :
        answer += 1
        heapq.heappush(ends, lastEnd)
        heapq.heappush(ends, end)
    
print(answer)
