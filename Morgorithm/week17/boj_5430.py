# 백준_문자열 : AC

import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for i in range(T) :
    order = input()
    n = int(input())
    temp = input().rstrip()
    arr = deque(temp[1:-1].split(","))
    rev = 0
    for o in order :
        if o == "R" :
            rev += 1
        if o == "D" :
            if n == 0 or len(arr) == 0 :
                print("error")
                break
            else :
                if rev % 2 == 0 :
                    arr.popleft()
                else : arr.pop()
    else :
        arr = [*arr]
        if rev % 2 == 0 :
            print("["+",".join(arr)+"]")
        else :
            arr.reverse()
            print("["+",".join(arr)+"]")