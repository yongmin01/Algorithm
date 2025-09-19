# [프로그래머스] 할인 행사

# 더러운 풀이
from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    
    dd = defaultdict(int)
    for i in range(10) :
        dd[discount[i]] += 1
    s, e = 0, 9
    while e <= len(discount) :
        for i in range(len(want)) :
            if dd[want[i]] != number[i] : break
        else : answer += 1
        
        dd[discount[s]] -= 1
        s += 1
        e += 1
        if e < len(discount) :
            dd[discount[e]] += 1
        
    return answer
    
# 깔끔한 풀이
from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    target = dict(zip(want, number))
    
    for i in range(len(discount)-9) :
        if target == Counter(discount[i:i+10]) : answer += 1
        
    return answer