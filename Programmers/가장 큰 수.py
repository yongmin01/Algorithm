# [프로그래머스] 정렬 > 가장 큰 수

def solution(numbers) :
    numbers = sorted(list(map(str, numbers)), key=lambda x : x*4, reverse=True)
    return str(int(''.join(numbers)))