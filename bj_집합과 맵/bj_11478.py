# 백준 집합과 맵_8 : 서로 다른 부분 문자열의 개수
import sys
s = sys.stdin.readline().rstrip()
results= set()
for l in range(len(s)) :
    for m in range(l, len(s)) :
        results.add(s[l:m+1])
print(len(results))