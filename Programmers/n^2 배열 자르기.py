# [프로그래머스] > n^2 배열 자르기

def solution(n, left, right):
    answer = []
    left_row = left // n
    left_col = left % n
    right_row = right // n
    right_col = right % n
    
    if left_row == right_row : # left와 right가 같은 행일 때
        for c in range(left_col, right_col+1) : # left의 열부터 right의 열까지만 돌면 됨
            answer.append(c+1 if c >= left_row else left_row+1)
        return answer
    
    for r in range(left_row, right_row+1) : # left와 right가 다른 행에 위치할 때 (left의 행 < right의 행)
        if r == left_row : # 현재 행이 left가 위치한 행일 경우 
            for c in range(left_col, n) : # 열은 left가 위치한 열부터 n까지 돌기
                answer.append(r+1 if r >= c else c+1)
        elif r < right_row :
            for c in range(n) :
                answer.append(r+1 if r >= c else c+1)
        else : # 현재 행이 right가 위치한 행일 경우 
            for c in range(right_col+1) : # 열은 0부터 right의 열까지만 순회
                answer.append(r+1 if r >= c else c+1)
    return answer