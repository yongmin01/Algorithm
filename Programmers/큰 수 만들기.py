# [프로그래머스] 탐욕법(Greedy) > 큰 수 만들기

def solution(number, k):
    number = list(map(int, number))
    stack = []
    for n in number :
        while k > 0 and stack and stack[-1] < n :
            stack.pop()
            k -= 1
        stack.append(n)
    if k > 0 :
        stack = stack[:-k]
    
    return ''.join(map(str, stack))
