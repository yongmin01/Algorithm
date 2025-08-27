# [프로그래머스] 완전탐색 > 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    arr = [i for i in range(len(dungeons))]
    for per in permutations(arr) :
        energy = k
        count = 0
        for dungeon in list(per) :
            need, use = dungeons[dungeon]
            if need <= energy :
                energy -= use
                count += 1
            else : 
                answer = count if count > answer else answer
                break
        else : 
            answer = len(dungeons)
            return answer
        
    return answer