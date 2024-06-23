# 백준 스택, 큐, 덱_11 : queuestack
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) # 큐인지 스택인지
B = list(map(int, sys.stdin.readline().split())) # 현재 큐스택에 들어있는 값
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
result = []

for i in reversed(range(N)) :
    if A[i] == 0 :
        result.append(B[i])
queue_amount = len(result)

for i in range(M) :
    if i < queue_amount :
        print(result[i], end=" ")
    else : print(C[i-queue_amount], end=" ")

