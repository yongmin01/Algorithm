# [백준] 그리디 > 수리공 항승

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
spots = sorted(list(map(int, input().split())))

curr = spots[0] - 0.5 + l
answer = 1
for spot in spots[1:] :
    if curr < spot :
        curr = spot - 0.5 + l
        answer += 1
    elif curr < spot + 0.5 :
        curr = spot + l
        answer += 1

print(answer)

