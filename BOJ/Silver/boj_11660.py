# [백준] DP, 누적합 > 구간 합 구하기 5

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for _ in range(n) :
    nums.append(list(map(int, input().split())))

# 누적합 구해놓기
acc = [[0 for _ in range(n)] for _ in range(n)]
for r in range(n) :
    for c in range(n) :
        if r == 0 : 
            if c == 0 : acc[r][c] = nums[r][c]
            else :
             acc[r][c] = acc[r][c-1] + nums[r][c]
        else : 
            if c == 0 :
                acc[r][c] = acc[r-1][c] + nums[r][c]
            else :
                acc[r][c] = acc[r-1][c] + acc[r][c-1] - acc[r-1][c-1] +  nums[r][c]

for _ in range(m) :
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(acc[x2-1][y2-1])
    elif x1 == 1 :
        print(acc[x2-1][y2-1] - acc[x2-1][y1-2])
    elif y1 == 1 :
        print(acc[x2-1][y2-1]- acc[x1-2][y2-1])
    else : print(acc[x2-1][y2-1] - acc[x2-1][y1-2] - acc[x1-2][y2-1] + acc[x1-2][y1-2])
