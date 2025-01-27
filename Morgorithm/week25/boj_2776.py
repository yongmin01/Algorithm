# 백준_이분 탐색 : 암기왕

import sys
input = sys.stdin.readline

def Binary_search(arr, target, start, mid, end) :
    if start > end : return False
    if arr[mid] == target : return True
    else :
        if arr[mid] < target :
            start = mid + 1
            mid = (end - start + 1) // 2 + start
            return Binary_search(arr, target, start, mid, end)
        elif arr[mid] > target :
            end = mid - 1
            mid = (end - start + 1) // 2 + start
            return Binary_search(arr, target, start, mid, end)


T = int(input())
for i in range(T) :
    N = int(input())
    nums = map(int, input().split())
    nums = sorted(nums)
    
    M = int(input())
    guess = map(int, input().split())

    s = 0
    e = N - 1
    m = N // 2
    for target in guess :
        if Binary_search(nums, target, s, m, e) :
            print(1)
        else : print(0)