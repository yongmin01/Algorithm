# [프로그래머스] 완전탐색 > 소수 찾기

from itertools import permutations
import math

def solution(numbers):
    comb = []
    for i in range(1, len(numbers)+1) :
        temp = permutations(numbers, i)
        for c in temp : 
            comb.append(c)
            
    num = set()
    for c in comb :
        num.add(int(''.join(c)))
    
    answer = []
    for i in num :
        if i == 0 or i == 1 :
            continue
        for n in range(2, int(math.sqrt(i))+1) :
            if i % n == 0 :
                break
        else : 
            answer.append(i)
    
    return len(answer)