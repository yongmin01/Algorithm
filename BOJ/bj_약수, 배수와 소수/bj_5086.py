# 백준 약수, 배수와 소수_1 : 배수와 약수
while True :
    N, M = [int(x) for x in input().split()]
    if N == 0 and M == 0 :
        break
    if N >= M :
        if N % M == 0 :
            print("multiple")
        else :
            print("neither")
    elif M >= N :
        if M % N == 0 :
            print("factor")
        else :
            print("neither")
