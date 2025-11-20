# [백준] 그리디 > 센서

import sys
input = sys.stdin.readline
import heapq

n = int(input())
k = int(input())

sensors = sorted(list(set(map(int, input().split(" ")))))


if k >= len(sensors) : # 집중국의 개수가 센서의 개수보다 많은 경우
    print(0) 
    exit()


d = []
answer = 0
for i in range(len(sensors)-1) :
    answer += sensors[i] - sensors[i+1]
    heapq.heappush(d, sensors[i] - sensors[i+1])
answer = -answer


while k > 1 :
    answer += heapq.heappop(d)
    k -= 1

print(answer)