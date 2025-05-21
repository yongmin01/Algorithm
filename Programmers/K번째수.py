# [프로그래머스] 정렬 > K번째수

def solution(array, commands):
    answer = []
    for c in commands :
        i, j, k = c
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
