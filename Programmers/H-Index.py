# [프로그래머스] 정렬 > H-Index

def solution(citations):
    answer = 0
    arr = [0] * (max(citations)+1)
    for a in citations :
        for i in range(a+1) :
            arr[i] += 1
    for i in range(len(arr)-1, 0, -1) :
        if arr[i] >= i :
            answer = i
            break
    return answer
