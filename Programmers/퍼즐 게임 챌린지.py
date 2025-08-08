# [프로그래머스] PCCP 기출문제 2번 > 퍼즐 게임 챌린지

def solution(diffs, times, limit):
    
    left = 1
    right = max(diffs)
    answer = right
    
    while left <= right :
        level = (left + right) // 2
        acc = 0
        for i in range(len(diffs)) :
            if level >= diffs[i] :
                acc += times[i]
            else :
                acc += (times[i]+times[i-1]) * (diffs[i]-level)  + times[i]
                
        if limit >= acc :
            if answer > level : 
                answer = level
            right = level - 1
        else :
            left = level + 1
            
    return answer