# [프로그래머스] 2024 KAKAO WINTER INTERNSHIP > 주사위 고르기

from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    answer = []
    combination = list(combinations(range(len(dice)), len(dice)//2))
    
    MAX = 0
    for comb_index in combination :
        a_dices = [dice[i] for i in comb_index]
        b_dices = [dice[i] for i in list(set(range(len(dice))).difference(set(comb_index)))]
        a_result = [sum(dices) for dices in product(*a_dices)]
        b_result = [sum(dices) for dices in product(*b_dices)]
        b_result.sort()
        
        a_counter = {}
        for a in a_result :
            if a in a_counter :
                a_counter[a] += 1
            else :
                a_counter[a] = 1
        
        cnt = 0
        a_counter_keys = list(a_counter.keys())
        for a in a_counter_keys :
            index = bisect_left(b_result, a)
            cnt += index * a_counter[a]
        
        if cnt > MAX :
            MAX = cnt
            answer = comb_index
        
    answer = [i + 1 for i in answer]
    return answer

