# [백준] 정렬 > 선 긋기

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n) :
    arr.append(list(map(int,input().split())))

arr.sort()
answer = 0
start, end = arr[0]
for i in range(1, n) :
    cur_start, cur_end = arr[i]
    if cur_start <= end :
        end = max(end, cur_end)
    else :
        answer += end - start
        start, end = arr[i]
answer += end - start

print(answer)