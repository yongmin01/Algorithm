# 백준 약수, 배수와 소수_3 : 약수들의 합
n = 1
while True :
    n = int(input())
    if n == -1 : break
    factors = []
    isPerfect = 0
    for x in range(1, n) :
        if n % x == 0 :
            factors.append(x)
    isPerfect = sum(factors)
    if isPerfect == n :
        print(n, "=", end=" ")
        for y in factors :
            print(y, end=" ")
            if y == factors[-1] :
                print()
                break
            print("+", end=" ")
    else : print(n, "is NOT perfect.")