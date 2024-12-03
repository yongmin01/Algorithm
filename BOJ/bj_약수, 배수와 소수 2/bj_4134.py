# 백준 약수, 배수와 소수 2_5 : 다음 소수
import sys
import math


def isPn(n) :
    if n <= 1 : return False
    elif n == 2 or n == 3 : return True
    else :
        for i in range(2, math.floor(n**0.5)+1) :
            if n % i == 0 :
                return False
        return True


n = int(sys.stdin.readline())
for _ in range(n) :
    c = int(sys.stdin.readline())
    if isPn(c) :
        print(c)
    else :
        while True :
            if isPn(c) :
                print(c)
                break
            else :
                c += 1

