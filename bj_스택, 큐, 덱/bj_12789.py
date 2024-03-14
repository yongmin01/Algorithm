# 백준 스택, 큐, 덱_5 : 도키도키 간식드리미
import sys
N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

turn = 1
stack = []
i = 0
while True:
    if line[i] == turn :
        turn += 1
        i += 1
    elif len(stack) != 0 and stack[-1] == turn :
        turn += 1
        stack.pop()
    else :
        stack.append(line[i])
        i += 1
    if i == N-1 : break

if len(stack) == 0 :
    print("Nice")
else :
    sortedStack = sorted(stack, reverse=True)
    for i in range(len(stack)) :
        if i == len(stack)-1 :
            print("Nice")
        if sortedStack[i] != stack[i] :
            print("Sad")
            break
    

