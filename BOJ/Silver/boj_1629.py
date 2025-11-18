# [백준] 수학, 분할정복을 이용한 거듭제곱 > 곱셈

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split(" "))

# sol1 : pow 내장함수 사용하기
# pow(base, exp, mod=None) 형태로, mod를 지정하면 "base의 exp 거듭제곱의 모듈러 mod 값"을 반환
# pow(base, exp) % mod 보다 빠르게 연산됨
print(pow(A, B, C))

# sol2 : 분할 정복 + 모듈러 연산의 분배 법칙
# 모듈러 연산의 곱셈 분배법칙 : (A * B) % C = (A%C * B%C) * C
def recursion(x, n) :
    if n == 1 : return x % C
    else :
        p = recursion(x, n//2)
        if n % 2 == 0 :
            return p * p % C
        else : return p * p * x % C

print(recursion(A, B) % C)
