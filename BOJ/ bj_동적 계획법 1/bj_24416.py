# 백준 동적 계획법1_1 : 알고리즘 수업 - 피보나치 수 1
# Python3로 제출하면 시간초과, PyPy3로 제출하면 정답.. 시간 복잡도 줄이는 코드도 다시 생각해보기

N = int(input())

# 재귀
recursion = 0
def fib(n) :
    global recursion
    if n == 1 or n == 2 :
        recursion += 1  
        return 1
    else :
        return (fib(n-1) + fib(n-2))
    
# DP
DP = 0
f = [1, 1]
def fibonacci(n) :
    global DP
    for i in range(2, n) :
        f.append(f[i-1] + f[i-2])
        DP += 1
    return

fib(N)
fibonacci(N)
print(recursion, DP)
