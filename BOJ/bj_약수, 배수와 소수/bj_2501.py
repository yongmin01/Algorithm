# 백준 약수, 배수와 소수_2 : 약수 구하기
N, K = [int(x) for x in input().split()]
factors = []
for x in range(1, N+1) :
    if N % x == 0 :
        factors.append(x)
if K > len(factors) :
    print(0)
else : print(factors[K-1])