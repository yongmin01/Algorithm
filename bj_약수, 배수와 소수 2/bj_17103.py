# 백준 약수, 배수와 소수 2_8 : 골드바흐 파티션

import sys

pn = [False, False] + [True] * 999999

# 소수 구하기
for i in range(2, 1000001) :
    if pn[i] :
        for i in range(i*2, 1000001, i) :
            pn[i] = False

# 골드바흐 파티션 구하기
N = int(sys.stdin.readline())
for _ in range(N) :
    T = int(sys.stdin.readline())
    count = 0
    for l in range(T//2 + 1):
        if pn[l] and pn[T-l] :
            count += 1
    print(count)