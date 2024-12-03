# 백준 조합론_4 : 이항 계수 1
import sys
import math

[N, K] = list(map(int, sys.stdin.readline().split()))

print(int(math.factorial(N)/(math.factorial(N-K)*math.factorial(K))))