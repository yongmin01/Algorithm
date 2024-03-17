# 백준 스택, 큐, 덱_8 : 요세푸스 문제 0
import sys
from collections import deque

[N, K] = map(int, list(sys.stdin.readline().split()))
people = deque(list(range(1, N+1)))
print("<", end="")
while len(people) != 1 :
    for i in range(K-1) :
        people.append(people[0])
        people.popleft()
    print(people[0], end=", ")
    people.remove(people[0])
print(people[0], ">", sep="")
