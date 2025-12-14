# [백준] 그리디 > 행복 유치원

import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
heights = list(map(int, input().split()))

chas = []
for i in range(1, n) :
    heapq.heappush(chas, [heights[i-1]-heights[i], i-1])

points = []

while k > 1 :
    cha, index = heapq.heappop(chas)
    heapq.heappush(points, index)
    k -= 1

cur, answer = 0, 0

while points :
    next = heapq.heappop(points)
    answer += heights[next] - heights[cur]
    cur = next+1

if cur != n-1 :
    answer += heights[n-1] - heights[cur]

print(answer)