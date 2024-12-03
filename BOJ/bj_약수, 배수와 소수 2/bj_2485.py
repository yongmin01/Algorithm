# 백준 약수, 배수와 소수 2_4 : 가로수
import sys

def GCD(a, b) :
    r = a % b
    mok = b
    while r != 0 :
        mok = r
        r = b % r
        b = mok
    return mok

N = int(sys.stdin.readline())
current = []
d = []
for i in range(N) :
    current.append(int(sys.stdin.readline()))
    if i >= 1 :
        d.append(current[-1]-current[-2])
distance = set(d)

count = 0
if len(distance) != 1 :
    A = max(distance)
    B = min(distance)
    g = GCD(A, B)
    for i in list(distance) :
        if i % g != 0 :
           g = GCD(max(g, i), min(g, i))
    
    for i in d :
        if i != g :
            count += i // g - 1
    print(count)
else :
    print(0)
