# 백준 백트래킹_8 : 스타트와 링크
# python3로는 실패..

import sys
input = sys.stdin.readline

start_power = 0
link_power = 0
min_val = 1e9

N = int(input())
S = []
for i in range(N) :
    S.append(list(map(int, input().split())))


def get_power(team, target, power) :
    if len(target) == 2 :
        return power + S[target[0]][target[1]]
        
    total_power = 0
    for i in team :
        target.append(i)
        total_power += get_power(team, target, power)
        target.pop()
    return total_power

def solution(idx, start) :
    if len(start) == N // 2 :
        # link 팀원 구하기
        link = []
        for i in range(N) :
            if i not in start :
                link.append(i)

        # 능력치 구하기
        global min_val
        min_val = min(abs(get_power(start, [], 0) - get_power(link, [], 0)), min_val)
        return
    
    for i in range(idx, N) :
        if i not in start :
            start.append(i)
            solution(i, start)
            start.pop()

    
solution(0, [])
print(min_val)
