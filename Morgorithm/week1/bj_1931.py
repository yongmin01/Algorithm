# 백준 그리디 알고리즘 : 회의실 배정

N = int(input())

meetings = []
for i in range(N) :
    [start, end] = map(int, input().split())
    meetings.append([start, end])

meetings.sort(key = lambda x: (x[1], x[0]))
result = 1
temp = 0
for i in range(N-1) :
    if meetings[temp][1] <= meetings[i+1][0] :
        result += 1
        temp = i + 1
print(result)
