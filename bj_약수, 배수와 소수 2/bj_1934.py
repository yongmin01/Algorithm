# 백준 약수, 배수와 소수 2_1 : 최소 공배수
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    [A, B] = list(map(int, sys.stdin.readline().split()))
    if A >= B :
        MAX = A
        MIN = B
    else :
        MAX = B
        MIN = A

    r = MAX % MIN
    while r != 0 : 
        temp = r
        r = MIN % r
        MIN = temp
    print(int(A*B/MIN))
    