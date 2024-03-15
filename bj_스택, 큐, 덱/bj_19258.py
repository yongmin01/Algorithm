# import sys
# from collections import deque
# N = int(sys.stdin.readline())
# queue =deque([])
# for i in range(N) :
#     order = sys.stdin.readline().split()
#     if order[0] == "push" :
#         queue.append(order[1])
#     elif order[0] == "pop" :
#         if len(queue) == 0 :
#             print(-1)
#         else :
#             print(queue.popleft())
#     elif order[0] == "size" :
#         print(len(queue))
#     elif order[0] == "empty" :
#         if len(queue) == 0 :
#             print(1)
#         else : print(0)
#     elif order[0] == "front" :
#         if len(order[0]) == 0 : print(-1)
#         else : print(queue[0])
#     elif order[0] == "back" :
#         if len(order[0]) == 0 : print(-1)
#         else : print(queue[-1])

# 왜 위 코드로 하면 런타임 에러(IndexError)가 날까..?

# 백준 스택, 큐, 덱_6 : 큐 2
from collections import deque
import sys

n = int(input())
queue = deque([])
for i in range(n):
    word = sys.stdin.readline().split()
    if word[0] == "push":
        queue.append(word[1])
    elif word[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
            del queue[0]
    elif word[0] == "size":
        print(len(queue))
    elif word[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)         
    elif word[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif word[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            