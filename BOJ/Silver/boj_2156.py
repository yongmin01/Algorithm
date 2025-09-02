import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n) :
    arr.append(int(input()))

if n < 3 :
    print(sum(arr))
elif n == 3 :
    print(max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2]))
else :
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2])
    for i in range(3, n) :
        dp[i] = max(dp[i-3] + arr[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    print(dp[-1])

# else :
#     dp =[[0 for _ in range(n)] for _ in range(2)]
#     dp[0][0] = arr[0]
#     dp[1][0] = arr[0]
#     dp[0][1] = arr[0] + arr[1]
#     dp[1][1] = arr[1]

#     for i in range(2, n) :
#         dp[0][i] = dp[1][i-1] + arr[i]
#         dp[1][i] = max(dp[0][i-2], dp[1][i-2]) + arr[i]
#         print(dp[0], "\n", dp[1])
#     print(max(max(dp[0]),max(dp[1])))