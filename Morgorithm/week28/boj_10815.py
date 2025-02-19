# 백준_자료구조, 정렬, 이분 탐색, 해시를 이용한 집합과 맵 : 숫자 카드

# sol 1
# import sys
# input = sys.stdin.readline

# N = int(input())
# has = list(map(int, input().split()))
# has.sort()

# M = int(input())
# guess = list(map(int, input().split()))

# for g in guess :
#     start = 0
#     mid = len(has) // 2
#     end = len(has) - 1
#     while start <= mid and mid <= end and start <= end :
#         if g == has[mid] : 
#             print(1, end=" ")
#             break
#         elif g < has[mid] :
#             end = mid - 1
#             mid = (start + end) // 2
#             continue
#         elif g > has[mid] :
#             start = mid + 1
#             mid = (start + end) // 2
#             continue
        
#     else :
#         print(0, end=" ")

# sol 2
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
has = [0 for _ in range(20000001)]
for card in cards :
    has[card] = 1 # 음수의 경우에느 음수 인덱스 자리에 체크하게 되므로 겹치지 X

M = int(input())
guess = list(map(int, input().split()))
for g in guess :
    if has[g] : print(1, end=" ")
    else : print(0, end=" ")