# [백준] 투 포인터 > 다이어트

G = int(input())
a = 2
answer = []
while a**2-(a-1)**2 <= G :
    if a**2-1 < G :
        a += 1
    elif a**2-1 == G :
        answer.append(a)
        a += 1   
    else :
        left, right = 1, a-1
        while 0 < left <= right < a:
            mid = (left+right) // 2
            if a**2 - mid**2 < G :
                right = mid -1
            elif a**2 - mid**2 == G :
                answer.append(a)
                break
            else : left = mid + 1
        a += 1

if len(answer) == 0 : print(-1)
else :
    for ans in answer : print(ans)

