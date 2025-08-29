# [프로그래머스] 행렬의 곱셈

def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    K = len(arr2)
    for r in range(len(arr1)) :
        for c in range(len(arr2[0])) :
            temp = 0
            for k in range(K) :
                temp += arr1[r][k]*arr2[k][c]
            answer[r].append(temp)
    return answer