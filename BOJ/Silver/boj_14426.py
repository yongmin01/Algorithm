# [백준] 이분 탐색, 트라이 > 접두사 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = []
for _ in range(n) :
    S.append(input().strip())
S.sort()

def di(word, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if word in S[mid] : 
            for i in range(len(word)) :
                if word[i] != S[mid][i] : break
            else : 
                return True
        if word < S[mid] :
            end = mid -1
        else : start = mid + 1
    return False

answer = 0 
for _ in range(m) :
    word = input().strip()
    if di(word, 0, n-1) :
        answer += 1
    
print(answer)