# [백준] 자료구조(스택) > 후위 표기식2

import sys
input = sys.stdin.readline
from collections import deque
from decimal import Decimal

n = int(input())
expression = input().strip()
operand = [int(input().strip()) for _ in range(n)]

stack = []
for i in range(len(expression)) :
    if 65 <= ord(expression[i]) <= 90 :
        stack.append(operand[ord(expression[i]) - 65])
    else :
        y = Decimal(stack.pop())
        x = Decimal(stack.pop())
        if expression[i] == "+" :
            stack.append(x+y)
        elif expression[i] == "-" :
            stack.append(x-y)
        elif expression[i] == "*" :
            stack.append(x*y)
        else :
            stack.append(Decimal(x) / Decimal(y))

print(round(stack.pop(), 2))

# 배열 대신 deque로 스택 구현
# 시간 차이는 없지만 메모리를 조금 더 쓴다

# import sys
# input = sys.stdin.readline
# from collections import deque
# from decimal import Decimal

# n = int(input())
# expression = input().strip()
# operand = [int(input().strip()) for _ in range(n)]

# q = deque()

# for i in range(len(expression)) :
#     if 65 <= ord(expression[i]) <= 90 :
#         q.append(operand[ord(expression[i])-65])
#     else :
#         y = Decimal(q.pop())
#         x = Decimal(q.pop())
#         if expression[i] == "+" :
#             q.append(x+y)
#         elif expression[i] == "-" :
#             q.append(x-y)
#         elif expression[i] == "*" :
#             q.append(x*y)
#         else :
#             q.append(Decimal(x) / Decimal(y))
# print(round(q.pop(), 2))
