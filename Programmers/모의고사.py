# [프로그래머스] 완전탐색 > 모의고사

def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0]
    
    for i in range(len(answers)) :
        # a가 이번 문제를 맞췄는지 확인
        if answers[i] == a[i%5] : correct[0] += 1
        # b가 이번 문제를 맞췄는지 확인
        if answers[i] == b[i%8] : correct[1] += 1
        # c가 이번 문제를 맞췄는지 확인
        if answers[i] == c[i%10] : correct[2] += 1
    
    MAX = max(correct)
    for i in range(3) :
        if correct[i] == MAX :
            answer.append(i+1)
    
    return answer