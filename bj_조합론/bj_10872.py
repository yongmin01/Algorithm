# 백준 조합론_3 : 팩토리얼

N = int(input())
a = 1
for i in range(1, N+1) :
    a *= i
print(a)