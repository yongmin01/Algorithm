import sys
input = sys.stdin.readline

n = int(input())
skills = []
for _ in range(n) :
    skills.append(list(map(int, input().split())))

start = []
link = []

