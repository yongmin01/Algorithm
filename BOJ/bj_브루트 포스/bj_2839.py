# 백준 브루트 포스 6 : 설탕 배달
import sys
N = int(sys.stdin.readline())
count = []

a = N // 5
b = N //3

for l in range(0, a+1) :
    for m in range(0, b+1) :
        if 5*l + 3*m == N :
            count.append(l + m) 

if len(count) == 0 :
    print(-1)
else : print(min(count))