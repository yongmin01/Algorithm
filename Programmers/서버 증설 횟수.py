# [프로그래머스] 서버 증설 횟수

def solution(players, m, k):
    answer = 0
    time = [0 for _ in range(24)]
    cur = 0
    for player in players :
        if player // m >= time[cur] :
            demand = player // m - time[cur]
            answer += demand
            for t in range(cur, cur+k) :
                if t < 24 :
                    time[t] += demand
        cur += 1
    return answer