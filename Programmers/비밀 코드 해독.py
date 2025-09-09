# [프로그래머스] 2025 프로그래머스 코드챌린지 1차 예선 > 비밀 코드 해독

from itertools import combinations

def solution(n, q, ans):
    answer = 0
    for comb in combinations(range(1, n+1), 5):
        for i in range(len(q)) :
            if len(set(comb).intersection(set(q[i]))) != ans[i] :
                break
        else : answer += 1
    
    return answer