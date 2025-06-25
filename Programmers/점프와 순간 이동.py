# [프로그래머스] Summer/Winter Coding(~2018) > 점프와 순간 이동

def solution(n):
    answer = 0
    while n > 0 :
        if n % 2 == 0 :
            n = n // 2
        else :
            n -= 1
            answer += 1
    return answer

# 효율성 문제 (시간 초과)
# def solution(n):
#     ans = 0
#     dis = [0 for _ in range(n+1)]
#     for i in range(1, n+1) :
#         if i % 2 == 0 :
#             dis[i] = min(dis[i-1]+1, dis[i//2])
#         else :
#             dis[i] = dis[i-1]+1
#     return dis[n]