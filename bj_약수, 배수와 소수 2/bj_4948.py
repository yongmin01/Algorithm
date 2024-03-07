# 백준 약수, 배수와 소수 2_7 : 베르트랑 공준
import sys
import math
def isPN(n) :
    if n < 2 : return False
    else :
        for i in range(2, math.floor(n**0.5)+1) :
            if n % i == 0 : return False
        return True
pn = []
for i in range(1, 246913) :
    if isPN(i) : pn.append(True)
    else : pn.append(False)

while True :
    count = 0
    n = int(sys.stdin.readline())
    if n == 0 : break
    for i in range(n+1, 2*n+1) :
        if pn[i-1] :
            count += 1
    print(count)