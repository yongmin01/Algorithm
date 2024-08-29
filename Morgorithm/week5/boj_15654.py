# 백준_백트래킹 : N과 M (5)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

seq = []

def dfs() :
    global seq
    if len(seq) == M :
        for x in seq:
            if x == seq[-1] :
                print(x)
            else : print(x, end =' ')
        seq.pop()
        return
    else :
        for i in range(N) :
            if nums[i] not in seq :
                seq.append(nums[i])
                dfs()
        if len(seq) > 0 :
                seq.pop()
                return

dfs()