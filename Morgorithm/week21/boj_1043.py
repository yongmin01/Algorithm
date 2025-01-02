# 백준_그래프 이론 : 거짓말

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [x for x in range(0, N+1)]
who_knows_the_truth = list(map(int, input().split())) # 진실을 아는 사람들

def find(n) :
    if parent[n] != n :
        return find(parent[n])
    return n
def union(a, b) :
    p1 = find(a)
    p2 = find(b)
    if p1 < p2 :
        parent[p2] = p1
    else : parent[p1] = p2

parties = []
answer = 0
# 파티에 참석한 사람들 입력받기
for i in range(M) :
    party = list(map(int, input().split()))
    parties.append(party)


if who_knows_the_truth[0] == 0 : # 진실을 아는 사람이 없는 경우 바로 출력
    print(M)
else :
    who_knows_the_truth = who_knows_the_truth[1:]
    for party in parties : # 파티를 전부 돌면서 각 파티에 입력한 사람들을 같은 그룹으로 묶기
        for i in range(1, party[0]) :
            union(party[i], party[i+1])

    for party in parties :
        break_outer = False
        for person in range(1, party[0]+1) : 
            for person_knows_truth in who_knows_the_truth :
                # 파티에 찹석한 사람과 진실을 아는 사람이 같은 그룹에 속하는지 판별하기
                if find(parent[party[person]]) == find(parent[person_knows_truth]) : 
                    break_outer = True
                    break
            if break_outer:
                break
        else : 
            answer += 1
    
    print(answer)