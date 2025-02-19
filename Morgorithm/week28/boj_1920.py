# 백준_자료구조, 정렬, 이분 탐색, 해시를 이용한 집합과 맵 : 수 찾기

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
guess = list(map(int, input().split()))

for g in guess :
    start = 0
    mid = len(A) // 2
    end = len(A) - 1

    while start <= mid and mid <= end and start <= end :
        if g == A[mid] :
            print(1)
            break
        elif g > A[mid] :
            start = mid + 1
            mid = (start + end) // 2
            continue
        elif g < A[mid] :
            end = mid - 1
            mid = (start + end) // 2
            continue
    else : print(0)