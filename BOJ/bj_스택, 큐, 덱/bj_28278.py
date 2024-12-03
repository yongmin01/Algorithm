# 백준 스택, 큐, 덱_1 : 스택 2
import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N) :
    order = sys.stdin.readline().rstrip()
    if int(order[0]) == 1 :
        stack.append(order.split()[1])
    elif int(order) == 2 :
        if len(stack) == 0 : print(-1)
        else : print(stack.pop())
    elif int(order) == 3 :
        print(len(stack))
    elif int(order) == 4 :
        if len(stack) == 0 : print(1)
        else : print(0)
    elif int(order) == 5 :
        if len(stack) == 0 : print(-1)
        else : print(stack[-1])