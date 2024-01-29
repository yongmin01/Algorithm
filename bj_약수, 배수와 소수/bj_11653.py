# 백준 약수, 배수와 소수_6 : 소인수분해
N = int(input())
factors = []
result = []

if N != 1 :
    for i in range(2, N+1) :
        if (N % i == 0) : 
            factors.append(i)
    
    for factor in factors :
            if factor == 2 :
                 result.append(factor)
            else :
                for i in range(2, factor) :
                    if factor % i == 0 :
                        break
                    else :
                        if i == factor-1 :
                            result.append(factor)
    for pf in result :
         while N % pf == 0 :
              print(pf)
              N = N // pf
