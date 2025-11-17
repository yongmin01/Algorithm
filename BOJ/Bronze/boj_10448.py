# [백준] 브루트포스 > 유레카 이론
import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

arr = []
for i in range(1, 45) :
    arr.append(i*(i+1)//2)

comb = combinations_with_replacement(arr, 3)

s = set()
for c in comb :
    s.add(sum(c))

T = int(input())
for _ in range(T) :
    K = int(input())
    if K in s : print(1)
    else : print(0)
