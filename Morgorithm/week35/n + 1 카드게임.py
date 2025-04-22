# [프로그래머스] 2024 KAKAO WINTER INTERNSHIP > n + 1 카드게임

from itertools import combinations
from collections import deque

def solution(coin, cards):
    round = 1
    n = len(cards)
    having = cards[0:(n//3)]
    having_combinations = list(combinations(having, 2))
    final_combinations = deque()
    for comb in having_combinations :
        a, b = comb
        if a + b == n + 1:
            final_combinations.append([a, b])
    keep = []
    curr = n//3
    
    while curr + 1 <= n-1 : # 뽑을 카드가 동나지 않았으면 
        keep.append(cards[curr])
        keep.append(cards[curr + 1])
        if len(final_combinations) > 0 : # having에서 두 장 낼 수 있는지 체크
            a, b = final_combinations[0]
            final_combinations.popleft()
            round += 1
        else : # having에서 한 장 keep에서 한 장 낼 수 있는지 체크
            if coin < 1 : # keep 더미에서 한 장 살 돈이 없으면 라운드 종료
                return round
            next_round = False
            for h in range(len(having)) :
                for k in range(len(keep)) :
                    if having[h] + keep[k] == n + 1:
                        h_index = cards.index(having[h])
                        if cards[h_index] != 0 :
                            cards[h_index] = 0
                            keep[k] = 0
                            coin -= 1
                            round += 1
                            next_round = True
                            break
                if next_round : break
            else : # keep으로 두 장 낼 수 있는지 체크
                if coin < 2 : # keep 더미에서 두 장 살 돈이 없으면 라운드 종료
                    return round
                next_round = False
                for i in range(0, len(keep) - 1) :
                    for l in range(i+1, len(keep)) :
                        if keep[i] + keep[l] == n + 1 :
                            keep[i] = 0
                            keep[l] = 0
                            coin -= 2
                            round += 1
                            next_round = True
                            break
                    if next_round : break
                else : return round
        curr += 2
                                
    return round
