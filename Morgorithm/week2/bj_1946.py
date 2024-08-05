# 백준_정렬 & 그리디 알고리즘 : 신입 사원

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    N = int(input())
    stack = []
    result = 1
    for l in range(N) :
        stack.append(list(map(int, input().split())))
    stack.sort()
    target = stack[0][1]
    for i in range(1, N) :
        if stack[i][1] < target :
            result += 1
            target = stack[i][1]
    print(result)
        
