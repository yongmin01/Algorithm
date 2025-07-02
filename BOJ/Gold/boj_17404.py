# [백준] 다이나믹 프로그래밍 > RGB거리 2

import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
results = []
for first_color in range(3) :
    INF = int(1e9)
    dp = [INF, INF, INF]
    dp[first_color]= cost[0][first_color]

    for l in range(1, n) :
        R = min(dp[1], dp[2]) + cost[l][0]
        G = min(dp[0], dp[2]) + cost[l][1]
        B = min(dp[0], dp[1]) + cost[l][2]
        dp = [R, G, B]
    
    answer = INF
    for last_color in range(3) :
        if last_color != first_color :
            if dp[last_color] < answer :
                answer = dp[last_color]
    results.append(answer)

print(min(results))

### 1차시도 ### 
# import sys
# input = sys.stdin.readline

# n = int(input())

# costs = []
# for _ in range(n) :
#     costs.append(list(map(int, input().split())))

# dp = [[costs[0][0], 'R'], [costs[0][1], 'G'], [costs[0][2], 'B']]

# for i in range(1, n-1) :
#     if i == n-2 :
#         R = [[costs[i][0] + dp[2][0], dp[2][1]], [costs[i][0] + dp[1][0], dp[1][1]]]
#         G = [[costs[i][1] + dp[2][0], dp[2][1]], [costs[i][1] + dp[0][0], dp[0][1]]]
#         B = [[costs[i][2] + dp[1][0], dp[1][1]], [costs[i][2] + dp[0][0], dp[0][1]]]
#         dp = [R, G, B]
#         break
#     # R 구하기
#     if dp[1][0] > dp[2][0]:
#         R = [costs[i][0] + dp[2][0], dp[2][1]]
#     else : 
#         R = [costs[i][0] + dp[1][0], dp[1][1]]

#     # G 구하기
#     if dp[0][0] > dp[2][0] :
#         G = [costs[i][1] + dp[2][0], dp[2][1]]
#     else :
#         G = [costs[i][1] + dp[0][0], dp[0][1]]
    
#     # B 구하기
#     if dp[0][0] > dp[1][0] :
#         B = [costs[i][2] + dp[1][0], dp[1][1]]
#     else :
#         B = [costs[i][2] + dp[0][0], dp[0][1]]

#     dp = [R, G, B]
# results = []
# # R
# for i in dp[0] :
#     if i[1] == 'G' : results.append(costs[-1][2] + i[0])
#     else : results.append(costs[-1][1] + i[0])

# # G
# for i in dp[1] :
#     if i[1] == 'R' : results.append(costs[-1][2] + i[0])
#     else : results.append(costs[-1][0] + i[0])

# # B
# for i in dp[2] :
#     if i[1] == 'R' : results.append(costs[-1][1] + i[0])
#     else : results.append(costs[-1][0] + i[0])

# print(min(results))


### 2차 시도 ###
# import sys
# input = sys.stdin.readline

# n = int(input())

# costs = []
# for _ in range(n) :
#     costs.append(list(map(int, input().split())))

# dp = [[costs[0][0], 'R'], [costs[0][1], 'G'], [costs[0][2], 'B']]

# for i in range(1, n) :
#     # R 구하기
#     if dp[1][0] > dp[2][0]:
#         R = [costs[i][0] + dp[2][0], dp[2][1]]
#     else : 
#         R = [costs[i][0] + dp[1][0], dp[1][1]]

#     # G 구하기
#     if dp[0][0] > dp[2][0] :
#         G = [costs[i][1] + dp[2][0], dp[2][1]]
#     else :
#         G = [costs[i][1] + dp[0][0], dp[0][1]]
    
#     # B 구하기
#     if dp[0][0] > dp[1][0] :
#         B = [costs[i][2] + dp[1][0], dp[1][1]]
#     else :
#         B = [costs[i][2] + dp[0][0], dp[0][1]]

#     dp = [R, G, B]

# colors = ['R', 'G', 'B']
# answer = int(1e9)
# for i in range(3) :
#     if dp[i][1] != colors[i] :
#         if answer > dp[i][0] :
#             answer = dp[i][0]
# print(answer)
