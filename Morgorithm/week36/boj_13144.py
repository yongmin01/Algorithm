# 백준_두 포인터 : List of Unique Numbers

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

has = [False for _ in range(max(arr)+1)]
result = 0
start = 0
end = 0
while start <= end and end < N :
    if not has[arr[end]] :
        has[arr[end]] = True
        result += end - start + 1
        end += 1
    else :
        has[arr[start]] = False
        start += 1
print(result)