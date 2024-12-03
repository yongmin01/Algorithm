# 백준 약수, 배수와 소수 2_3 : 분수 합
import sys

[A, B] = list(map(int, sys.stdin.readline().split()))
[C, D] = list(map(int, sys.stdin.readline().split()))
A = A * D + C * B
B = B * D

if A >= B :
        MAX = A
        MIN = B
else :
    MAX = B
    MIN = A

# 최대공약수 구하기
r = MAX % MIN
mok = MIN
while r != 0 : 
    mok = r
    r = MIN % r
    MIN = mok

print(A // mok, B // mok)