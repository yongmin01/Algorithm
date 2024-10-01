# 백준_스택 : 스택수열

import sys
input = sys.stdin.readline

n = int(input())
result = []
stack = []
current = 1
for i in range(n) :
    num = int(input())
    while current <= num :
        stack.append(current)
        result.append("+")
        current += 1
    
    if num == stack[-1] :
        stack.pop()
        result.append("-")
    else :
        break
if len(result) == n*2 :
    for i in range(len(result)) :
        print(result[i])
else : print("NO")


