# 백준 심화 2_3 : 붙임성 좋은 총총이

import sys
N = int(sys.stdin.readline())
dance = []
for i in range(N) :
    [a, b] = sys.stdin.readline().rstrip().split()
    if a in dance or b in dance :
        dance.append(a)
        dance.append(b)
    elif a == "ChongChong" or b == "ChongChong" :
        dance.append(a)
        dance.append(b)
    
    
print(len(set(dance)))