# [프로그래머스] > 요격 시스템

def solution(targets):
    answer = 1
    targets.sort()
    top = targets[0]
    
    for target in targets[1:] :
        if top and top[1] > target[0] :
            if top[1] < target[1] :
                top = [target[0], top[1]]
            else : top = [target[0], target[1]]
        else :
            top = target
            answer += 1
            
    return answer