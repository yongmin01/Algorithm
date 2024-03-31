# 백준 재귀_1 : 팩토리얼 2

N = int(input())
a = 1
def factorial (n) :
    if (n <= 1) :
        return 1
    return n * factorial(n-1)

print(factorial(N))