# 백준 스택, 큐, 덱_3 : 괄호
import sys
T = int(sys.stdin.readline())
for i in range(T) :
    test = list(sys.stdin.readline())
    stack = []
    for l in test :
        if l == "(" :
            stack.append(l)
        elif l == ")" :
            if len(stack) == 0 :
                print("NO")
                break
            else : 
                stack.pop()
        else :
            if len(stack) == 0  :
                print("YES")
            else : print("NO")
        