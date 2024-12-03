# 백준 정렬_10 : 나이순 정렬
import sys
N = int(sys.stdin.readline())
members = []
for i in range(N) :
    [age, name] = sys.stdin.readline().rstrip().split()
    members.append([int(age), name])

members.sort(key=lambda x: x[0])
for i in range(N) :
    print(members[i][0], members[i][1])