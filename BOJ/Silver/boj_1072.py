# [백준] 이분 탐색 > 게임
# 부동 소수점 오차를 고려해야 하는 문제

import math
import decimal
X, Y = map(int, input().split())
result = 0

if X == Y :
    result = -1
else :
    start = 1
    end = 1000000000
    target = math.floor(decimal.Decimal(Y) / decimal.Decimal(X) * 100)
    while start <= end :
        mid = (start + end) // 2
        x = X + mid
        y = Y + mid
        if math.floor(decimal.Decimal(y) / decimal.Decimal(x) * 100) > target :
            result = mid
            end = mid - 1
        else :
            start = mid + 1
if result == 0 :
    print(-1)
else :
    print(result)




# X, Y = map(int, input().split())
# result = 0

# if X == Y :
#     result = -1
# else :
#     start = 1
#     end = 1000000000
#     target = Y*100//X
#     while start <= end :
#         mid = (start + end) // 2
#         x = X + mid
#         y = Y + mid

#         if y*100//x > target :
#             result = mid
#             end = mid - 1
#         else :
#             start = mid + 1
# if result == 0 :
#     print(-1)
# else :
#     print(result)

