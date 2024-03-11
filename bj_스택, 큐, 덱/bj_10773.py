# 백준 스택, 큐, 덱_2 : 제로
import sys
K = int(sys.stdin.readline())
stack = []
for i in range(K) :
    order = int(sys.stdin.readline())
    if order != 0 :
        stack.append(order)
    elif order == 0 :
        stack.pop()
print(sum(stack))