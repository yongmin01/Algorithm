# [프로그래머스] 스택/큐 > 올바른 괄호

from collections import deque

def solution(s):
    stack = deque()
    for i in s :
        if i == '(' :
            stack.append('(')
        else :
            if not stack : return False
            if stack[-1] == "(" :
                stack.pop()
    if len(stack) > 0 : return False
    else : return True
    