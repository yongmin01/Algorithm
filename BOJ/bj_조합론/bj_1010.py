# 백준 조합론_5 : 다리 놓기
import math
import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T) :
    [N, M] = list(map(int, sys.stdin.readline().split()))
    print(int(math.factorial(M)/(math.factorial(M-N)*math.factorial(N))))
