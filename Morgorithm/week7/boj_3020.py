# 백준_누적 합 : 개똥벌레

import sys
input = sys.stdin.readline

N, H = map(int, input().split())
hurdle = [0]
jong = [0] * (H+2)
suk = [0] * (H+2)

for i in range(N) : 
    temp = int(input())
    if i % 2 == 0 :
        jong[H-temp+1] += 1
    else :
        suk[temp] += 1

for h in range(1, H+1) :
    jong[h] = jong[h-1] + jong[h]

for h in range(H, 0, -1) :
    suk[h] = suk[h+1] + suk[h]

for h in range(1, H+1) :
    hurdle.append(jong[h] + suk[h])

min_val = min(hurdle[1:H+1])
count = hurdle[1:H+1].count(min_val)
print(min_val, count)
