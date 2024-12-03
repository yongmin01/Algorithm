# 백준 약수, 배수와 소수 2_6 : 소수 구하기
import sys
import math

def isPN(n) :
    if n < 2 : return False
    for i in range(2, math.floor(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    return True

[M, N] = list(map(int, sys.stdin.readline().split()))
pn = [False]
for i in range(1, N+1) :
    if isPN(i) :
        pn.append(True)
    else: pn.append(False)

for i in range(M, N+1) :
    if pn[i] :
        print(i)