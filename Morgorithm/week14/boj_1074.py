# 백준_분할정복, 재귀 : Z

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def quadrant(N, r, c, low_level) :
    if r // low_level == 0 or (r // low_level == 1 and r % low_level == 0) :
        if c // low_level == 0 or (c // low_level == 1 and c % low_level == 0) :
            return 1
        else :
            return 2
    else :
        if c // low_level == 0 or (c // low_level == 1 and c % low_level == 0) :
            return 3
        else :
            return 4
result = 0

while N > 0 :
    low_level = 2 ** (N-1)
    x = quadrant(N, r+1, c+1, low_level)
    if N == 1 :
        result += x * low_level * low_level
    else :
        result += (x-1) * low_level * low_level

    N -= 1
    if x == 2 : c -= low_level
    elif x == 3 : r -= low_level
    elif x == 4 : 
        c -= low_level
        r -= low_level

print(result-1)