# [백준] 이분 탐색 > 슬라임 잡고 레벨 업!

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N = int(input())
    total = N * (N+1) // 2
    start = 1
    end = N
    answer = 0
    while start <= end :
        mid = (start+end) // 2
        if mid * (mid+1)  <= total :
            answer = mid
            start = mid + 1
        else :
            end = mid - 1
    print(answer+1)
