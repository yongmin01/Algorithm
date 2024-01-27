# 백준 약수, 배수와 소수_4 : 소수 찾기
N = int(input())
inputs = [int(x) for x in input().split()]
prime = len(inputs)

for x in inputs :
    if x == 1 :
        prime -= 1
    else :
        for i in range(2, x) :
            if x % i == 0 :
                prime -= 1
                break

print(prime)