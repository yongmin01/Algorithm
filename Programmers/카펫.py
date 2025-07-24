# [프로그래머스] 완전탐색 > 카펫

def solution(brown, yellow):
    answer = []
    for i in range(yellow, 0, -1) :
        if yellow % i == 0 :
            if 2 * ((i+2) + yellow // i) == brown :
                answer.append(i+2)
                answer.append(yellow//i+2)
                break
                
    return answer