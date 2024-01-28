# 백준 약수, 배수와 소수_5 : 소수
M = int(input())
N = int(input())

primeNums = []
for prime in range(M, N+1) :
    if prime == 1 :
     continue
    elif prime == 2 :
        primeNums.append(prime)
    else :
        for i in range(2, prime) :
            if prime % i == 0 :
                break
            elif i == prime -1 :
                primeNums.append(prime)
if len(primeNums) == 0 :
    print(-1)
else :
    print(sum(primeNums))
    print(min(primeNums))
