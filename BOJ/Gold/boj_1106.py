# [백준] DP > 호텔

import sys
input = sys.stdin.readline

c, n = map(int, input().split())
info = []
for _ in range(n) :
    info.append(list(map(int, input().split())))

dp = [[0] for _ in range(n)]
answer = 100001
money = 1
while True :
    for i in range(len(info)) :
        cost, customer = info[i]
        if i == 0 :
            dp[i].append((money // cost) * customer)
            if dp[i][-1] >= c and answer > money :
                answer = money
        else :
            if money >= cost :
                dp[i].append(max(dp[i-1][money], dp[i][money-cost]+customer))
            else :
                dp[i].append(max(dp[i-1][money], dp[i][money-1]))
            if dp[i][-1] >= c and answer > money :
                answer = money
    if answer != 100001 : 
        print(answer)
        break
    else : money += 1

# import sys
# input = sys.stdin.readline
# import heapq
# import math
# c, n = map(int, input().split())

# # 마케팅 효율이 낮은 순서로 정렬 및 저장("얻을 수 있는 고객수 / 홍보비" 가 작은 순서)
# # 이 순서로 탐색을 해야 모든 경우를 탐색할 수 있음 -> 아님;; 단지 dp 메모리 크기를 미리 정하는데 도움이 될 뿐
# # ex 
# pq = []
# for _ in range(n) :
#     cost, customer = map(int, input().split())
#     heapq.heappush(pq, (customer/cost, cost, customer))

# dp = [[0 for _ in range(math.ceil(c / pq[0][2])*pq[0][1]+1)] for _ in range(n)]

# answer = len(dp[0])
# for m in range(1, len(dp[0])) :
#     dp[0][m] = pq[0][2] * (m // pq[0][1])
#     if dp[0][m] >= c and answer > m : answer = m

# for city in range(1, len(pq)) :
#     _, cost, customers = map(int, pq[city])
    
#     for m in range(1, len(dp[0])) :
#         if m >= cost :
#             dp[city][m] = max(dp[city-1][m], dp[city][m-cost]+customers)
#         else : dp[city][m] = max(dp[city-1][m], dp[city][m-1])

#         if dp[city][m] >= c and answer > m : 
#             answer = m

# print(answer)
