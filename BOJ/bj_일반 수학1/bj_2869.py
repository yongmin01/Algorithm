# 백준 일반 수학1_7 : 달팽이는 올라가고 싶다
import math
[A, B, V] = [int(x) for x in input().split()]
print(math.ceil((V-B) / (A-B)))