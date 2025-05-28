# [백준] DP > 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N)]
stuff = []
for _ in range(N) :
    stuff.append(list(map(int, input().split())))
stuff.sort()
for w in range(stuff[0][0], K+1) :
    dp[0][w] = stuff[0][1]
for s in range(1, N) :
    w, v = stuff[s]
    for l in range(K+1) :
        if l >= w :
            dp[s][l] = max(dp[s-1][l-w] + v, dp[s-1][l])
        else :
            dp[s][l] = dp[s-1][l]

print(dp[N-1][K])


# 물건이 무한대로 있다고 잘못 생각 했을 때 풀이

# N, K = map(int, input().split())
# dp = [0 for _ in range(K+1)]
# stuff = []
# for _ in range(N) :
#     stuff.append(list(map(int, input().split())))
# stuff.sort()
# print(stuff)

# for limit in range(stuff[0][0], K+1) :
#     if limit % stuff[0][0] == 0 :
#         dp[limit] = dp[limit-stuff[0][0]] + stuff[0][1]
#     else :
#         dp[limit] = dp[limit-1]
# print("무게", stuff[0][0], "가치", stuff[0][1], "인 물건을 채운 뒤")
# print(dp)
# for s in stuff[1:] :
#     w, v = s
#     print("무게", w, "가치", v, "인 물건 담기기")
#     for limit in range(w, K+1) :
#         if dp[limit-w] != 0 :
#             dp[limit] = max( dp[limit], dp[limit-w] + v)
#         else :
#             dp[limit] = max(dp[limit], v)
#         print(limit, "만큼 채운 뒤", dp)
# print(dp[-1])
