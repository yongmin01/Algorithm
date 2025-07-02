# [프로그래머스] 귤 고르기

def solution(k, tangerine):
    dict = {}
    for t in tangerine :
        if t in dict :
            dict[t] += 1
        else : dict[t] = 1
    dict = sorted(dict.items(), key=lambda x : x[1], reverse=True)

    sum = 0
    answer = 0

    while sum < k :
        sum += dict[answer][1]
        answer += 1
    
    return answer