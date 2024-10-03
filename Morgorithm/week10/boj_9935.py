# 백준_스택 : 문자열 폭발

str = list(input())
bomb = list(input())

strlen = len(str)
bomblen = len(bomb)

stack = []

for i in range(strlen) :
    stack.append(str[i])
    stacklen = len(stack)
    if stack[-1] == bomb[-1] and stacklen >= bomblen :
        if stack[stacklen - bomblen:] == bomb :
            for i in range(bomblen) :
                stack.pop()

if len(stack) > 0 :
    print("".join(stack))
else :
    print("FRULA")
