# 백준_문자열 & 두 포인터 : 회문

import sys
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T) :
    s = input().rstrip()
    front = 0
    rear = len(s) - 1
    removedTimes = 0
    d = "front"
    s_front = 0
    s_rear = len(s) - 1
    while front < rear :
        if s[front] == s[rear] :
            front += 1
            rear -= 1
            continue
        if removedTimes == 1 and d == "front" :
            print(2)
            break
        if removedTimes == 0 and s[front] == s[rear - 1] :
            s_front = front
            s_rear = rear
            rear -= 1
            removedTimes += 1
            d = "rear"
            continue
        if removedTimes == 1 and d == "rear": 
            front = s_front
            rear = s_rear
            removedTimes -= 1
        if removedTimes == 0 and s[front + 1] == s[rear] :
            s_front = front
            s_rear = rear
            front += 1
            removedTimes += 1
            d = "front"
            continue
        else : 
            print(2)
            break
    else :
        if removedTimes == 0 :
            print(0)
        else : print(1)
