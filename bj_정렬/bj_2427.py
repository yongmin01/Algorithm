# 백준 정렬_6 : 소트인사이드

import sys
N = list(map(int, sys.stdin.readline().rstrip()))
N.sort(reverse=True)
for i in N :
    print(i, end="")