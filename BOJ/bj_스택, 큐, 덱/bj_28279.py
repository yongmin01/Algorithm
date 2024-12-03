# 백준 스택, 큐, 덱_9 : 덱 2

import sys
from collections import deque

N = int(sys.stdin.readline().strip())
d = deque([])
for i in range(N) :
    order = sys.stdin.readline().rstrip()
    if order[0] == "1" : d.appendleft(order.split()[1])
    elif order[0] == "2" : d.append(order.split()[1])
    elif order == "5" : print(len(d))
    elif order == "6" :
        if len(d) == 0 : print("1")
        else : print("0")
    else :
        if len(d) == 0 : print("-1")
        else :
            if order == "3": print(d.popleft())
            elif order == "4" : print(d.pop())
            elif order == "7" : print(d[0])
            elif order == "8" : print(d[-1])
