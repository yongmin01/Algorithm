# [백준] 이분 탐색 > 예산

import sys
input = sys.stdin.readline

n = int(input())

requests = list(map(int, input().split()))
budget = int(input())

requests.sort()
start = 0
end = budget

answer = start
while start <= end :
    mid = (start+end) // 2
    temp = 0
    t_answer = 0
    for request in requests :
        if request <= mid :
            temp += request
            t_answer = request
        else :
            temp += mid
            t_answer = mid
    if temp > budget :
        end = mid - 1
    else :
        start = mid + 1
        answer = answer if answer > t_answer else t_answer

print(answer)