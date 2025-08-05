# [프로그래머스] 2019 카카오 개발자 겨울 인턴십 > 징검다리 건너기

def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    mid = left + (right - left) // 2
    
    while left <= right :
        mid = left + (right - left) // 2
        jump = 0
        for i in range(len(stones)) :
            if stones[i] - mid > 0 :
                jump = 0
                continue
            else :
                jump += 1
                if jump == k :
                    right = mid - 1
                    break
        else :
            left = mid + 1
            if mid + 1 > answer :
                answer = mid + 1
    return answer
            
       