# [프로그래머스] 두 원 사이의 정수 쌍

import math
def solution(r1, r2):
    answer = 0
    big, small = 0, 0
    
    for x in range(1, r2) :
        big += int(math.sqrt(pow(r2, 2) - pow(x, 2)))
        
    temp = 0
    for x in range(1, r1) :
        temp = math.sqrt(pow(r1, 2) - pow(x, 2))
        if temp == int(temp) :
            small += int(temp) - 1
        else : small += int(temp)
    
    answer = (big - small + (r2-r1+1)) * 4
    return answer