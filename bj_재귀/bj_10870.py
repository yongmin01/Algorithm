# 백준 재귀_2 : 피보나치 수 5 
n = int(input())

def F (n) :
    if n == 0 :
        return 0
    elif n == 1 : 
        return 1
    else :
        return F(n - 1) + F(n - 2)
print(F(n))