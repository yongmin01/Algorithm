# 백준 입출력과 사칙연산_9 : 나머지
[A, B, C] = map(int, input().split())
                                         
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)