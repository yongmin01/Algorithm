# 백준_그리디 알고리즘 : 주유소

import sys
input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0
min_price = price[0]
for i in range(N) :
    if i <= N - 2 :
        if price[i] <= min_price :
            min_price = price[i]
        answer += min_price * distances[i]
print(answer)