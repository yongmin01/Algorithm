# Softeer : CPTI

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cptis = {}
for _ in range(N) :
    key = int(input().rstrip(), 2)
    if key in cptis :
        cptis[key] += 1
    else : cptis[key] = 1

answer = 0

for cpti in cptis.keys() :
    answer += cptis[cpti] * (cptis[cpti] - 1) / 2 # 0자리 다른 경우 (동일한 CPTI인 사람들끼리 이룰 수 있는 쌍 카운트)
    for i in range(M) : # 1자리만 다른 경우
        new_num = cpti ^ 1 << i
        if new_num in cptis and cpti > new_num :
            answer += cptis[cpti] * cptis[new_num]
        for j in range(i+1, M) : # 2자리가 다른 경우
            new_num2 = new_num ^ 1 << j
            if new_num2 in cptis and cpti > new_num2:
                answer += cptis[cpti] * cptis[new_num2]

print(int(answer))
