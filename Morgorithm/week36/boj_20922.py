# 백준_두 포인터 : 겹치는 건 싫어

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

dict = {}

for n in arr :
    dict[n] = 0

s = 0
e = K-1
for i in range(e+1) :
    dict[arr[i]] += 1


answer = 1
while s <= e :
    if e + 1 >= len(arr) : # e가 끝이라서 더이상 갈 수 없을 때
        break
    else :
        if dict[arr[e+1]] + 1 <= K : # e가 더 가도 괜찮을 때 
            e += 1
            dict[arr[e]] += 1
            if e-s+1 > answer : 
                answer = e-s+1
        else : # e가 더 가면 K개를 넘어가서 s가 움직여야 할 때
            if s+1 > e :
                dict[arr[s]] -= 1
                s += 1
                e += 1
                dict[arr[e]] += 1
                continue
            
            dict[arr[s]] -= 1
            s += 1
print(answer)