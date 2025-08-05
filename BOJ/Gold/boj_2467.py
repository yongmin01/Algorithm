# [백준] 이분 탐색 > 용액

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = [1000000000, 1000000000]
    
for i in range(n) :
    target = arr[i]
    start = i + 1
    end = n-1
    while start <= end :
        mid = start + (end - start) // 2
        if target + arr[mid] == 0 :
            answer = [target, arr[mid]]
            break
        elif target + arr[mid] > 0 :
            end = mid - 1
        else :
            start = mid + 1
        if abs(answer[0]+answer[1]) > abs(target+arr[mid]) :
            answer = [target, arr[mid]]

print(answer[0], answer[1])