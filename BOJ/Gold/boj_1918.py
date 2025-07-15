# [백준] 자료구조, 스택 > 후위 표기식

import sys
input = sys.stdin.readline

exp = input().strip()
stack = []
answer = []

for i in exp :
    if 65 <= ord(i) <= 90 :
        answer.append(i)

    elif i == '+' or i == '-' :
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
            if stack and stack[-1] == '(' :
                break
        stack.append(i)

    elif i == '*' or i == '/' :
            if stack and (stack[-1] == '*' or stack[-1] == '/') :
                 answer.append(stack.pop())
            stack.append(i)


    elif i == '(' :
        stack.append(i)

    else : 
        while stack and stack[-1] != '(' :
            answer.append(stack.pop())
        stack.pop()

while stack :
     answer.append(stack.pop())

print(''.join(answer))